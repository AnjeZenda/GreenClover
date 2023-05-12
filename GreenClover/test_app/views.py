from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse
import requests
from rest_framework import generics
from test_app.models import Snippet
from test_app.serializers import SnippetSerializer
from rest_framework.parsers import JSONParser
import io

class ProductList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


def get_info(lang='ru', order_by='slug', fields='id,slug,name'):
    # url = f'https://kudago.com//public-api/v1.4/event-categories/?lang={lang}&order_by={order_by}&fields={fields}'
    url = 'https://kudago.com/public-api/v1.2/event-categories/?lang=ru'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    return data

def events(request: HttpRequest):
   # data = get_info()
    stream = io.BytesIO(request.body)
    json_str = JSONParser().parse(stream)
    return JsonResponse({'data': json_str})

def index(request):
    return HttpResponse("Index")