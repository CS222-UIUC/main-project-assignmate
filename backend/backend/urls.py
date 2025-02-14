"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# useful in displaying index.html template
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('email/', include('email_handler.urls')),
    path('backend/', include('app1.urls')),  # app_auth urls

    path('login/google/', views.custom_login, name='custom_login'),
    path('login/', views.custom_login, name='login'),
    path('logout', LogoutView.as_view()), # default Django logout view at /logout

    path('', TemplateView.as_view(template_name='index.html')),
    # all OAuth operations will be performed under this route
    path('accounts/', include('allauth.urls')),

    
    path('pl/', include('scraper.urls')),


    # path('assignments/', get_all_assignments, name='get_all_assignments'),
    # path('courses/<int:course_id>/assignments/', get_assignments_by_course, name='get_assignments_by_course'),
    # path('assignments/<int:assignment_id>/', get_assignment_by_id, name='get_assignment_by_id'),
    # path('login/', canvas_login, name='canvas_login'),
    # path('callback/', canvas_callback, name='canvas_callback'),
    path('canvasapp/', include('canvasapp.urls'))
]
