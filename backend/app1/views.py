# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse



# app1/views.py
from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views import View
from .forms import CustomSignupForm
from .validators import validate_illinois_email

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                validate_illinois_email(user.email)  # Ensure the email is valid
                login(request, user)
                return redirect('home')  # Redirect to home after successful login
            except ValidationError as e:
                return HttpResponse(f"Invalid email: {e}", status=400)
        else:
            return HttpResponse("Invalid credentials", status=401)

def index(request):
    return HttpResponse("This works")





# Create your views here.

# def home(request):
#     return render(request, 'home.html')

# def login_view(request):
#     return redirect('social:begin', 'google-oauth2')

# def logout_view(request):
#     from django.contrib.auth import logout
#     logout(request)
#     return redirect('/')

# def index(request):
#     return HttpResponse("This works")

#make a seperate class
#create a login post request
