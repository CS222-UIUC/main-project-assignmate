# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse



# app1/views.py
from django.shortcuts import redirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
def custom_login(request):
    adapter = GoogleOAuth2Adapter(request)
    client = OAuth2Client(request, adapter.client_id, adapter.secret)
    return redirect(client.get_redirect_url())
