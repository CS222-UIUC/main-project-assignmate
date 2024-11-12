from django.urls import path
from .views import DataView

urlpatterns = [
    path('data/', DataView.as_view(), name='scrape_data'),
]
