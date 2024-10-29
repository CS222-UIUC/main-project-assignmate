from django.urls import path
from .views import scrape_data_view

urlpatterns = [
    path('scrape/', scrape_data_view, name='scrape_data'),
]
