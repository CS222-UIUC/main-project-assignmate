# myapp/pipeline.py

def validate_illinois_email(backend, uid, user=None, *args, **kwargs):
    if user and user.email and not user.email.endswith('@illinois.edu'):
        raise Exception('You must use an @illinois.edu email address to register.')