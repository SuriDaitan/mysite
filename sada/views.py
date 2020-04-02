from django.shortcuts import render, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, "base.html")