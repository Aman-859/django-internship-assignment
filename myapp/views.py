from django.shortcuts import render , redirect
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponse
from .tasks import send_welcome_email
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TelegramUser
from django.http import JsonResponse
import requests
from decouple import config

# Create your views here.

#public api 
@api_view(['GET'])
@permission_classes([AllowAny])
def public_api(request):
    return Response({'message ': 'This Is Public Api !'})

#private api
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_api(request):
    return Response({'message':f'Welcome {request.user.username} , you are in private api ! '})


# web based login  
def login_view(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('protected')
            else:
                return HttpResponse('Invalid credentials.')

        except Exception as e:
            print(f"Login error: {e}")
            return HttpResponse('Something went wrong. Please try again.')

    return render(request, 'login.html')



#protected view 
def protected_view(request):
    return HttpResponse(f'''
        <h1>Welcome, {request.user.username}</h1>
        <p>This is a protected view.</p>
         <a href="/logout/">Logout</a>
    ''')


#logout
def logout_view(request):
    logout(request)
    return redirect('login') 



# celery integration  with sending email 
def register_view(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username', '')
            email = request.POST.get('email', '')
            password = request.POST.get('password', '')

            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            user.save()

            # calling celery for background email process
            try:
                send_welcome_email.delay(email)
            except Exception as e:
                print(f"Error sending welcome email: {e}")

            return redirect('login')

        except Exception as e:
            print(f"Error in user registration: {e}")
            return render(request, 'register.html', {'error': 'Something went wrong. Please try again.'})

    return render(request, 'register.html')




# Telegram bot which store username and telegram id if client send /start
@csrf_exempt
def telegram_webhook(request):
    if request.method == 'POST':
        try:

            data = json.loads(request.body.decode('utf-8'))

            message = data.get('message' ,{})
            text = message.get('text' , '')
            username = message.get('from' , {}).get('username'  , '')
            telegram_id = message.get('from',{}).get('id', '')


            if text == '/start' and username :
                TelegramUser.objects.create(username=username , telegram_id= telegram_id)
                send_telegram_message(telegram_id , f"Hi {username}! Your Telegram ID ({telegram_id}) has been successfully saved in our database.")

                return JsonResponse({'status' : 'ok'} ,status=200)
        except Exception as e:
            return JsonResponse({'staus' : 'invalid'} ,status=400)
        
    return JsonResponse({'status': 'invalid'}, status=400)

# response function 
def send_telegram_message(chat_id , text):
    token = config('Token')
    url =  f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id" :  chat_id,
        "text" :text
    }

    try:
        requests.post(url, json=payload)
    except Exception as e :
        print("Error sending message:", e)
            

