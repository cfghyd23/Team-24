from django.shortcuts import render
from .models import login
from rest_framework import status
from rest_framework 

# Create your views here.

def index(request):
    return render(request,"index.html")

def intern_login(request):



