from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(email):
    subject = "Welcome to our website"
    message = "Thanks for registering. Enjoy our services!"
    from_email = "no-reply@example.com"
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return f"Email sent to {email}"