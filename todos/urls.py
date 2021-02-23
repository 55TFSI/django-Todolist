from django.conf.global_settings import MEDIA_ROOT
from django.conf.urls import url
from django.urls import path
from django.views.static import serve

from . import views

app_name='todos'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    #path('<int:todo_id>/delete', views.delete, name='delete'),
    #path('<int:todo_id>/update', views.update, name='update'),
    #path('add/', views.add, name='add'),
    path('index', views.index, name='index'),
    path('finish', views.finish, name='finish'),
    path('list_todo', views.list_todo, name='list_todo'),
    path('delete_todo', views.delete_todo, name='delete_todo'),
    path('reverse_todo', views.reverse_todo, name='reverse_todo'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('update_todo', views.update_todo, name='update_todo'),
]