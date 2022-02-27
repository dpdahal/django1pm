from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'pages/home/home.html')

def about(request):
    return render(request, 'pages/about/about.html')
