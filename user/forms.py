from django import forms

from todos.models import Category


class Add_Category_Form(forms.Form):

    name = forms.CharField(max_length=100,)
    pic = forms.ImageField(required=True)



class Update_Category_Form(forms.Form):
    name = forms.CharField(max_length=100,)
    pic = forms.ImageField(required=True,)