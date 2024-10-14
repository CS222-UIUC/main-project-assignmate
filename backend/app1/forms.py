from allauth.account.forms import SignupForm
from .validators import validate_illinois_email

class CustomSignupForm(SignupForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_illinois_email(email)  # Call your custom validator
        return email
