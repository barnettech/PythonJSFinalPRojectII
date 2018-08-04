from django.urls import path
from .models import Food

from . import views

# register all the url routes in the views.py file
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("play_game", views.play_game, name="play_game"),
]
