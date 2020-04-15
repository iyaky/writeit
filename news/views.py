from django.shortcuts import render, get_object_or_404
from .models import News


def news(request):
    news = News.objects
    return render(request, 'news/news.html', {'news':news})

def detail(request, news_id):
    detailnews = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html', {'news':detailnews})
