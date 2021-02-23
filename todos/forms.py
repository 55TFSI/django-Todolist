from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from django.http import request

from django.shortcuts import get_object_or_404

from todos.models import Category, Todo

CHOICES = [('1', 'yes'),
           ('0', 'no')]
class Todo_add_form(forms.Form):
    title = forms.CharField(max_length=100,)
    is_completed = forms.ChoiceField(choices=CHOICES)
    category = forms.ChoiceField()




