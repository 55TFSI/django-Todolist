from markdown  import markdown
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from todos.models import Category, Category_delete
from user.forms import Add_Category_Form, Update_Category_Form, Article_form
from user.models import Article

def index(request):
    user = request.user
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
        form = Add_Category_Form(request.POST,request.FILES)

        if form.is_valid():
            name = form.cleaned_data['name']
            pic = request.FILES.get('pic')
            if not pic:
                Category.objects.create(name=name,user=user).save()
            else:
                Category.objects.create(name = name, pic = pic, user = user).save()
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

    if category.pic.name == 'categorypics/pic01.jpg':
        category.delete()
    else:
        Category_delete(category)
        category.delete()

    return redirect('/user/list_categories')

@login_required
def list_articles(request):

    user = request.user

    articles = Article.objects.filter(user = user)

    context = {'type': 'list_articles','Articles':articles}

    return render(request, 'userbase.html', context)

@login_required
def show_article_detail(request):

    article_id = request.GET.get('id')
    article = get_object_or_404(Article,pk=article_id)
    article.content = markdown(article.content,
                            extensions=[
                            # 包含 缩写、表格等常用扩展
                            'markdown.extensions.extra',
                            # 语法高亮扩展
                            'markdown.extensions.codehilite',
                            ])

    context = {'article':article}

    return render(request, 'article.html', context)

@login_required
def add_articles(request):
    if request.method == 'GET':
        # return a form for user
        form = Article_form()
        # get user_created_categories and return a for users form to fill
        return render(request, 'articleform.html', {'form': form, 'type': 'add_articles'})
    # post method from form html

    else:
        user = request.user
        #get infos from form
        form = Article_form(request.POST,request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            thumbnail = request.FILES.get('thumbnail')
            description = form.cleaned_data['description']
            content = form.cleaned_data['content']
            if not thumbnail:
                Article.objects.create(title=title,description=description,content =content,user= user).save()
            else:
                Article.objects.create(title=title,description=description,content =content,thumbnail=thumbnail,user =user).save()
        else:
            error = form.errors
            return render(request,'articleform.html',{'form':form,'error':error,'type':'add_articles'})

        return redirect('/user/list_articles')

def update_articles(request):

    if request.method == 'GET':
        article_id = request.GET.get('article_id',None)
        article = get_object_or_404(Article,pk =article_id)
        update_articles.article = article

        form = Article_form()
        context = {'article':article,'form':form,'type':'update_article'}

        # get user_created_categories and return a for users form to fill
        return render(request, 'articleform.html', context)
    else:

        # get infos from form
        form = Article_form(request.POST,request.FILES)

        if form.is_valid():
            article = update_articles.article
            pic = request.FILES.get('thumbnail',None)
            if not pic:
                article.title = form.cleaned_data['title']
                article.description  = form.cleaned_data['description']
                article.content = form.cleaned_data['content']

            else:
                article.title = form.cleaned_data['title']
                article.description = form.cleaned_data['description']
                article.content = form.cleaned_data['content']
                article.thumbnail = pic

            article.save()

        else:
            article = update_articles.article
            error = form.errors
            return render(request, 'articleform.html', {'form': form, 'error': error, 'type': 'update_article','article':article})

        return redirect('/user/list_articles')

@login_required
def delete_articles(request):
    article_id = request.GET.get('article_id',None)
    article = get_object_or_404(Article,pk = article_id)
    article.delete()
    return redirect('/user/list_articles')