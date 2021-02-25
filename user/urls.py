from django.conf.urls import url
from django.urls import path, include
from django.views.static import serve

from todoApp.settings import MEDIA_ROOT
from . import views

app_name='user'
urlpatterns = [
    path('', views.index, name='index'),
    path('list_categories', views.list_categories, name='list_categories'),
    path('add_categories', views.add_categories, name='add_categories'),
    path('update_categories', views.update_categories, name='update_categories'),
    path('delete_categories', views.delete_categories, name='delete_categories'),
    # articles
    path('list_articles', views.list_articles, name='list_articles'),
    path('show_article_detail', views.show_article_detail, name='show_article_detail'),
    path('add_articles', views.add_articles, name='add_articles'),
    path('update_articles', views.update_articles, name='update_articles'),
    path('delete_articles', views.delete_articles, name='delete_articles'),

]