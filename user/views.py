from django.shortcuts import render

# Create your views here.
from todos.models import Category
from user.forms import Add_Category_Form


def home(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'userbase.html')

def list_categories(request):
    # get user
    user = request.user

    # get categories created by user
    categories = Category.objects.filter(user_id = user.id)
    context = {'categories':categories, 'type':'list_categories'}
    return render(request, 'userbase.html',context)

def add_categories(request):
    if request.method == 'GET':
        # return a form for user
        form = Add_Category_Form()
        # get user_created_categories

        return render(request, 'forms.html', {'form': form, 'type': 'add_category'})

    return render(request, 'userbase.html')