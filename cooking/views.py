from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request, *args, **kwargs):
    name = request.GET.get('name', 'world')
    return HttpResponse(f'Hello, {name}')
