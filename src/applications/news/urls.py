from django.urls import path
from applications.news.views.main_news import main_news
from applications.news.apps import NewsConfig
from applications.news.views.post import PostView

app_name = NewsConfig.label


urlpatterns = [
    path('', main_news, name='main_news'),
    path('<int:pk>', PostView.as_view(), name="news-detail"),
]
