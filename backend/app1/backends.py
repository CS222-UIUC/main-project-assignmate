from allauth.account.auth_backends import AuthenticationBackend
from django.core.exceptions import ValidationError
from .validators import validate_illinois_email

class CustomAuthenticationBackend(AuthenticationBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)
        if user is not None:
            validate_illinois_email(user.email)
        return user
