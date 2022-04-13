from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm 
# Create your views here.

# @login_required
def index(request):
	if request.user.is_authenticated:
		name=request.user.username
	return render(request, "login/index.html", locals())


def login(request):
    if request.method=='POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/index/')
                message = '登入成功！'
            else:
                message = '帳號尚未啟用！'
        else:
            message = '登入失敗！'
    return render(request, "login/login.html",locals())

def logout(request):
	auth.logout(request)
	return redirect('/index/')



def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('yes !!successfully')
            return redirect('/')  #重新導向到登入畫面
    context = {
        'form': form
    }
    return render(request, 'login/register.html', context)
