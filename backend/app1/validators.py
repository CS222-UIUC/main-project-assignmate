from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_illinois_email(value):
    if not value.endswith('@illinois.edu'):
        raise ValidationError(
            _('Please use a valid @illinois.edu email address.'),
            params={'value': value},
        )
