from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ip_change(request):
    return HttpResponse("<h1> im changing default django baseUrl...</h1>")

    
    