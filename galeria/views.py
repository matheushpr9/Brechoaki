from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<H1>Brechoaki</H1><p>Bem vindo!</p>')