
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
    path("중랑구" , views.중랑구) ,
    path("동작구" , views.동작구) ,
    path("노량진로" , views.노량진로) ,
    path("매봉로" , views.매봉로) ,
    path("장승배기로" , views.장승배기로) ,
    path("상도로" , views.상도로) ,
]