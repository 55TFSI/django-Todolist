from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    update_at = models.DateTimeField('Updated', auto_now=True)
    isCompleted = models.BooleanField(default=False)
    user = models.ForeignKey(User, to_field='id', on_delete= models.CASCADE)
    category = models.ForeignKey('Category',to_field = 'id',on_delete=models.CASCADE)


    def __str__(self):
        return self.title
'''
class User_Category(models.Model):
        user = models.ForeignKey(User, to_field='id', on_delete= models.CASCADE)
        category = models.ForeignKey('Category', to_field='id',on_delete= models.CASCADE)
'''
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Category(models.Model):
    name = models.CharField(max_length=30,default=True)
    pic = ProcessedImageField(upload_to='categorypics',
                              default='categories/pic01.jpg',
                              processors=[ResizeToFill(506,295)])
    user = models.ForeignKey(User,to_field = 'id',on_delete=models.CASCADE,default= 2)


@receiver(pre_delete, sender=Category)
def Category_delete(instance, **kwargs):
    instance.pic.delete(False)