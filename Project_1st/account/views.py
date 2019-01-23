from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *

def index(request):
    return redirect('/login')

def index_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return render(request, 'account/logfail.html',)
    elif request.user.is_authenticated:
        return redirect('/index')
    else:
        return render(request, 'account/login.html')

def signup(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            new = Account()
            check = new.register(signup_form)
            if check:
                return redirect('/')
            else:
                return render(request, 'account/signup_fail.html')
        else:
            return render(request, 'account/signup_fail2.html')
    elif request.user.is_authenticated:
        return render(request, 'account/signup_fail3.html')
    else:
        signup_form = SignupForm()
        return render(request, 'account/signup.html', {'signupform':signup_form})

def logout_ques(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'account/logoutQues.html',)

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    logout(request)
    return render(request, 'account/logoutSuc.html',)
