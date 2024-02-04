from django.shortcuts import render
from django.http import HttpResponse
from . import meal_lists

# Create your views here.

def index(request):
    return HttpResponse("someday this will run meal_lists")