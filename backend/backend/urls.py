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
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path('oauth/', include('social_django.urls', namespace='social')),
#     path('', include('app1.urls')),  # Include your app's URLs
# ]
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView # useful in displaying index.html template
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/',include('app1.urls')), #app_auth urls

    path('', TemplateView.as_view(template_name='index.html')),
    path('accounts/', include('allauth.urls')), # all OAuth operations will be performed under this route
    path('logout', LogoutView.as_view(), name = 'logout') # default Django logout view at /logout
]