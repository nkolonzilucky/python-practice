from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class ExternalDataView(APIView):
    def get(self, request):
        # Replace this with your mock API URL
        url = 'https://jsonplaceholder.typicode.com/posts'
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return Response(data)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=500)


# Create your views here.
