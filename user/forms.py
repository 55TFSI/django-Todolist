from django import forms




class Add_Category_Form(forms.Form):
    name = forms.CharField(max_length=100,)
    pic = forms.ImageField(required=False)



class Update_Category_Form(forms.Form):
    name = forms.CharField(max_length=100,)
    pic = forms.ImageField(required=False,)