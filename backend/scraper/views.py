from django.shortcuts import render
from .utils import scrape_prairie_learn_data
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DataView(APIView):
    def get(self, request):
        data = scrape_prairie_learn_data()
        return Response(data, status=status.HTTP_200_OK)

# Create your views here.
