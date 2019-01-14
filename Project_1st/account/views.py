from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from .forms import *

def index_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                django_login(request,user)
                return redirect('index.html')
            login_form.add_error(None, 'Wrong ID or PW')
    else:
        login_form = LoginForm()
    context={
        'login_form': login_form,
    }
    return render(request, 'login.html')
