from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):

    return HttpResponse("<h1> Welcome Guru 123!! </h1>")
