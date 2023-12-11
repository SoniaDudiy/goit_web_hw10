from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm, LoginForm

...

@login_required
def logoutuser(request):
    logout(request)
    return redirect(to='hw_project:main')