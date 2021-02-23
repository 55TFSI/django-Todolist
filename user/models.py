from django.contrib.auth.models import User
from django.db import models

# Create your models here.
'''
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=20)
'''
class Quote(models.Model):
    author = models.CharField(max_length=35)
    content = models.TextField()
    user = models.ForeignKey(User, to_field='id', on_delete = models.CASCADE)