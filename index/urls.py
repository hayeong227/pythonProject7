
from django.urls import path , include
from . import views

urlpatterns = [
    path("index" , views.index) ,
    path("login" , views.login) ,
    path("signup" , views.signup) ,
    path("Q_A" , views.Q_A) ,
    path("boardwrite" , views.boardwrite) ,
    path("view1" , views.view1) ,
    path("소개" , views.소개) ,
]