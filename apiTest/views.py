from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    api_request = requests.get("https://korey-movie-rater-backend.herokuapp.com/api/ratings/")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error, data not loading"
    return HttpResponse(api['detail'])