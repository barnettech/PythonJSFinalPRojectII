from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Highscore
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

# after game ends post highscore to the model Highscore
def post_highscore(request):
   print('posting the highscore')
   score = request.POST.get('score', 0)
   print(f"score is {score}")
   H = Highscore(besttime=int(score), username=request.user.username)
   H.save()
   return HttpResponse("Success!") # Sending an success response

def view_highscores(request):
    #will order them in desc order and return the top 10 scores
    highscores=Highscore.objects.all().order_by('-besttime')[:10]
    print(highscores)
    return render(request, 'highscores.html', {'highscores':highscores})
