"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
 
from django.urls import path
from .views import public_api , private_api , login_view , protected_view , logout_view , register_view , telegram_webhook
urlpatterns = [
    path('api/public/' , public_api , name='public_api'),
    path('api/private/' , private_api , name='private_api'),

    #web based login
    path('login/' ,login_view , name='login' ),
    path('protected/',protected_view , name='protected'),
     path('logout/', logout_view, name='logout'),

    #celery 
    path('register/' ,register_view , name='register' ),

    #telegram bot
    path('telegram-webhook/', telegram_webhook, name='telegram_webhook')
]
