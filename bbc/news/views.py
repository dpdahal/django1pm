from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.

def index(request):
    data = {
        'categoryData': Category.objects.all()
    }
    return render(request, 'pages/home/home.html', data)


def about(request):
    return render(request, 'pages/about/about.html')


def news_details(request, slug):
    data = {
        'newsData': News.objects.get(slug=slug),
        'categoryData': Category.objects.all()
    }
    return render(request, 'pages/news-details.html', data)


def cat_list(request, cat_id):
    data = {
        'getCatNewsData': News.objects.filter(cat_id=cat_id),

    }
    return render(request, 'pages/cat-list.html', data)


def news_search(request):
    if request.GET['criteria'] == "":
        return redirect('index')

    else:
        criteria = request.GET['criteria']
        data = News.objects.filter(Q(title__icontains=criteria) | Q(cat_id__cat_name=criteria))
        content = {
            'newsData': data
        }

        return render(request, 'pages/news-list.html', content)


def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        Contact.objects.create(email=email, subject=subject, message=message)
        send_mail(subject, message, email, ['laravel3pm@gmail.com'])
        messages.success(request, 'Successfully contact')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return render(request, 'pages/contact.html')
