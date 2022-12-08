from django.shortcuts import render, HttpResponse


# Create your views here.
def hello_admin(request):
    return HttpResponse("Hello Admin")
