# email_handler/management/commands/send_scheduled_email.py

from django.core.mail import send_mail
from django.conf import settings
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Send a test email'

    def handle(self, *args, **kwargs):
        subject = "Hello from Django Email Handler"
        message = "This is a test email sent from our Django email handler."
        recipient_list = ["xyz@gmail.com"]  # Replace with the actual recipient email

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient_list,
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS("Email sent successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Failed to send email: {e}"))
