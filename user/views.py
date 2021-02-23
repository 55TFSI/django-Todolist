from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todos.models import Category, Category_delete
from user.forms import Add_Category_Form, Update_Category_Form


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

@login_required
def add_categories(request):
    if request.method == 'GET':
        # return a form for user
        form = Add_Category_Form()
        # get user_created_categories and return a for users form to fill
        return render(request, 'forms.html', {'form': form, 'type': 'add_category'})
    # post method from form html
    else:
        user = request.user
        #get infos from form
        form = Add_Category_Form(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            pic = request.FILES.get('pic')
            Category.objects.create(name = name, pic = pic, user = user)
        else:
            error = form.errors
            return render(request,'forms.html',{'form':form,'error':error,'type':'add_category'})

        return redirect('/user/list_categories')


@login_required
def update_categories(request):
    if request.method == 'GET':
        # return a form for user
        form = Update_Category_Form()
        #remeber category_id
        category_id = request.GET.get('category_id', None)
        update_categories.category_id = category_id

        # get user_created_categories and return a for users form to fill
        return render(request, 'forms.html', {'form': form, 'type': 'update_category'})
    else:
        user = request.user
        # get infos from form
        form = Update_Category_Form(request.POST,request.FILES)

        if form.is_valid():

            category_id = update_categories.category_id
            category = get_object_or_404(Category, pk=category_id)

            pic = request.FILES.get('pic',None)
            if not pic:
                category.name = form.cleaned_data['name']
            else:
                Category_delete(category)
                category.name = form.cleaned_data['name']
                category.pic = pic

            category.save()

        else:
            error = form.errors
            return render(request, 'forms.html', {'form': form, 'error': error, 'type': 'update_category'})

        return redirect('/user/list_categories')




@login_required
def delete_categories(request):
    category_id = request.GET.get('category_id',None)
    category = get_object_or_404(Category,pk = category_id)

    Category_delete(category)
    category.delete()

    return redirect('/user/list_categories')