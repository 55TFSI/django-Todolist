from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

'''
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=20)
'''
class Quote(models.Model):
    author = models.CharField(max_length=35)
    content = models.TextField()
    user = models.ForeignKey(User, to_field='id', on_delete = models.CASCADE)

class Article(models.Model):
    title = models.CharField(help_text='title', max_length=60)
    description = models.CharField(help_text='description', max_length=300, blank=True)
    thumbnail = ProcessedImageField(upload_to='articleimgs',
                                    default='categorypics/pic01.jpg',
                                    processors=[ResizeToFill(506,295)]
                                    )

    content = models.TextField(help_text='content')
    user = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)

