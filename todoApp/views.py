from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from todos.models import Todo


def index(request):
    pass
    return render(request, 'index.html')
def login(request):
    pass
    return render(request,'login.html')

def login_handle(request):
    # recieve datas:
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 业务：校验
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if user.is_active:
            #put user into request
            auth.login(request,user)
            # 跳转到list_todo 首页

            return redirect('/todos/list_todo')
        else:
            return render(request,'login.html',{'errormsg':'plz connect admin to active this account'})

    # 无此用户 return to login with msg
    else:
        return render(request,'login.html',{'errormsg':'incorrect username or password'})
