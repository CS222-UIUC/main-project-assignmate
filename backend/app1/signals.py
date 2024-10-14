# app1/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .validators import validate_illinois_email

User = get_user_model()  # Get the user model

@receiver(post_save, sender=User)
def validate_user_email(sender, instance, created, **kwargs):
    if created:  # Only validate when a user is created
        validate_illinois_email(instance.email)  # Call the custom validator
