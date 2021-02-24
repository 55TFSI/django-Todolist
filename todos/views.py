from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from user.models import Quote
from .forms import Todo_add_form
from .models import Todo, Category
from django.http import HttpResponseRedirect, HttpResponse
'''
class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('-created_at')
'''
def index(request):
    return render(request, 'index.html')

# ttodo filter user from session
@login_required
def list_todo(request):
    # initialize context
    #e.g {categories:[
    #           {name: daily,
    #            lists: [{notdone: [tod1:{title: xxx,  done: false}}],
    #                    done:[{title: xxx,  done: false}]]}
    #            pic:
    #                ]
    context = {'all':[],'user':''}
    # get user id
    u_id  = request.user.id
    u_name =request.user.username
    #get quote
    import  random
    quote = Quote.objects.filter(user = request.user)
    quote = random.choice(quote)
    context.update({'quote':quote})

    # get categoies that user created
    user_categories = Category.objects.filter(user_id = u_id)
    context['user'] = u_name
    for user_category in user_categories:
        done_list = []
        not_done_list = []
        todos = Todo.objects.filter(user_id = u_id,category_id = user_category.pk)#,created_at__day = timezone.now().day)

        for todo in todos:
            if todo.isCompleted == True:
                done_list.append(todo)
            else:
                not_done_list.append(todo)

        context['all'].append({'name':user_category.name ,'pic_url':user_category.pic,'done_list':done_list, 'not_done_list':not_done_list})

    return render(request, 'base.html', context)

@login_required
def finish(request):
    # get user id from session
    u_id = request.session.get('_auth_user_id')
    # get title
    todo_id = request.GET.get('id',None)
    #find atodo by id and user id (some of the user have same todolist e.g. getbath)
    todo = get_object_or_404(Todo,id=todo_id,user_id = u_id)

    #update  the status to 1
    todo.isCompleted = 1
    todo.save()
    return redirect('/todos/list_todo')

def reverse_todo(request):
    # get title
    todo_id = request.GET.get('todo_id', None)
    #find atodo by title and user id (some of the user have same todolist e.g. getbath)
    todo = get_object_or_404(Todo,id=todo_id)
    #update  the status to 1
    todo.isCompleted = 0
    todo.save()
    return redirect('/todos/list_todo')

@login_required
def add_todo(request):

    if request.method == 'GET':
        def getchoices(request):
            r = [('', '----')]
            u_id = request.session.get('_auth_user_id')
            for obj in Category.objects.filter(user_id=u_id):
                r = r + [(obj.id, obj.name)]
            return r

        form = Todo_add_form()
        # get user_created_categories
        form.fields['category'].choices = getchoices(request)
        return render(request,'forms.html',{'form': form,'type':'add_todo'})
    else:
        user_id = request.session.get('_auth_user_id')
        is_completed = True if request.POST.get('is_completed',False) == '1' else False
        title  = request.POST.get('title',None)
        category_id = request.POST.get('category','Undfined')
        category = Category.objects.get(id =category_id,user_id = user_id)

        Todo.objects.create(title = title, category = category, user_id = user_id, isCompleted =is_completed)

        return redirect('/todos/list_todo')

@login_required
def delete_todo(request):
    #get  user_id title from request url and session
    u_id, todo_id = request.session.get('_auth_user_id'), request.GET.get('todo_id',None)
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('/todos/list_todo')

# update  and add need a form    POST  includingtodo.features
@login_required
def update_todo(request):
    if request.method == 'GET':
        def getchoices(request):
            r = [('', '----')]
            u_id = request.session.get('_auth_user_id')
            for obj in Category.objects.filter(user_id=u_id):
                r = r + [(obj.id, obj.name)]
            return r

        todo_id = request.GET.get('todo_id')
        update_todo.todo_id = todo_id
        form = Todo_add_form()
        # get user_created_categories
        form.fields['category'].choices = getchoices(request)
        return render(request, 'forms.html', {'form': form, 'type': 'update_todo'})
    else:

        todo_id = update_todo.todo_id
        is_completed = True if request.POST.get('is_completed', False) == '1' else False
        title = request.POST.get('title', None)
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        Todo.objects.filter(pk=todo_id).update(title =title, category =category, isCompleted =is_completed)
        return redirect('/todos/list_todo')