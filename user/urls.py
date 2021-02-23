from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from todoApp.settings import MEDIA_ROOT
from . import views

app_name='user'
urlpatterns = [
    path('', views.index, name='index'),
    path('list_categories', views.list_categories, name='list_categories'),
    path('add_categories', views.add_categories, name='add_categories'),
]