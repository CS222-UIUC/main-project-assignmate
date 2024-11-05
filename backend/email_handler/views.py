from django.shortcuts import render

# Create your views here.
# email_handler/views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    subject = "Hello from Django Email Handler"
    message = "This is a test email sent from our Django email handler."
    recipient_list = ["annapoorna.narayan@gmail.com"]  # Replace with the actual recipient email

    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Failed to send email: {e}")
