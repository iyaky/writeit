from django.shortcuts import render
from .models import News


def news(request):
    news = News.objects
    return render(request, 'news/news.html', {'news':news})
