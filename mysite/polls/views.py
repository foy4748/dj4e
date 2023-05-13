#from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(req):
    # return HttpResponse("From Polls App")
    return HttpResponse("Hello, world. a35e2f4a is the polls index.")
