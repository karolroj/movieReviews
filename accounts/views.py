from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError

from accounts.forms import UserCreateForm, AuthenticateUser


# Create your views here.
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupaccount.html',
                              {'form': UserCreateForm, 'error': 'Username already taken. Choose another username.'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Passwords do not match'})


def logoutaccount(request):
    logout(request)
    return redirect('home')


def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': AuthenticateUser})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': AuthenticateUser,
                                                         'error': 'Username or password are invalid'})
        login(request, user)
        return redirect('home')
