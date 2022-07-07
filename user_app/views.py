from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import *

# Create your views here.

def user_registration(request):
    registration_form = CreateUserForm()

    if request.method == 'POST':
        submitted_form = CreateUserForm(request.POST)

        if submitted_form.is_valid():
            submitted_form.save()
        
            return redirect('login')

        else:

            return HttpResponse(submitted_form.errors)

    context = {
        'form' : registration_form
    }

    return render(request, 'users/register.html', context=context)


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Invalid Credentials")

    return render(request, 'users/login.html')


def user_logout(request):

    logout(request.user)

    return redirect('login')