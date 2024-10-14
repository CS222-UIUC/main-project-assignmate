# app1/urls.py

from django.urls import path, include
from . import views
#from .views import home, login_view, logout_view

# urlpatterns = [
#     path('', home, name='home'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
# ]

urlpatterns = [
    path('home/', views.index),
]


