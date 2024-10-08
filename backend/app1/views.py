from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return redirect('social:begin', 'google-oauth2')

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('/')