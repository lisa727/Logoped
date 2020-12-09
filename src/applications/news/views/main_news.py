from applications.news.models import Articles
from django.shortcuts import render


def main_news(request):
    news = Articles.objects.all()
    return render(request, 'news/main_news.html', {'news':news})
