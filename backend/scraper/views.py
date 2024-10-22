from django.shortcuts import render
from django.http import JsonResponse
from .utils import scrape_prairie_learn_data

def scrape_data_view(request):
    # Run the scraper
    data = scrape_prairie_learn_data()
    
    # Return the scraped data as JSON
    return JsonResponse(data, safe=False)

# Create your views here.
