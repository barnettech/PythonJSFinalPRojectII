from django.urls import path
from .models import Highscore

from . import views

# register all the url routes in the views.py file
urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signup, name="signup"),
    path("play_game", views.play_game, name="play_game"),
    path("post_highscore", views.post_highscore, name="post_highscore"),
]
