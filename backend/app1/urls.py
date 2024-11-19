# app1/urls.py

from django.urls import path, include
# from . import views
#from .views import LoginVieww
#from .views import CustomLoginView, CustomSignupView
from django.contrib.auth import views as auth_views
from app1 import views

urlpatterns = [
    #path('home/', views.index),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('login/', views.custom_login, name='custom_login'),
    
    # path("", views.home),
    # path("logout", views.logout_view)
]