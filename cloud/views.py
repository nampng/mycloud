from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, 'cloud/index.html', {})

def docs(response):
    return render(response, 'cloud/docs.html', {})

def pics(response):
    return render(response, 'cloud/pics.html', {})