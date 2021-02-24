from django import forms

from todos.models import Category
from user.models import Article


class Add_Category_Form(forms.Form):

    name = forms.CharField(max_length=100,)
    pic = forms.ImageField(required=True)



class Update_Category_Form(forms.Form):
    name = forms.CharField(max_length=100,)
    pic = forms.ImageField(required=False,)

class Article_form(forms.Form):
    title = forms.CharField( max_length=60)
    description = forms.CharField( max_length=300,)
    thumbnail = forms.ImageField()

    content = forms.CharField(widget=forms.Textarea)
