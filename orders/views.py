from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Food, Order, Order_Number
from django.db import models
from django.contrib.auth.models import User
from django import forms
from .forms import UserCreateForm
import datetime
import requests

# at the homepage, prompt to either login or register
def index(request):
    if request.user.username is not None:
      return redirect('play_game')
    return render(request, 'play_game.html', {})

# form to register for the site
def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        # save the registration form.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('play_game')
    else:
        form = UserCreateForm()
    return render(request, 'signup.html', {'form': form})

# view existing orders at this route.
def play_game(request):
   return render(request, 'JSgame.html')
   #return render(request, 'JSgame.html', {'orders':orders})
