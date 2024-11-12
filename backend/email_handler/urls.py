# email_handler/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('email/', views.send_test_email, name='send_email'),
]
