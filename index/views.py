from django.shortcuts import render

def index( request ) :
    return render( request , "index.html")
def login( request ) :
    return render( request , "login.html")
def signup( request ) :
    return render( request , "signup.html")
def Q_A( request ) :
    return render( request , "Q_A.html")
def boardwrite( request ) :
    return render( request , "boardwrite.html")
def view1( request ) :
    return render( request , "view1.html")
def 소개( request ) :
    return render( request , "소개.html")
def 중랑구( request ) :
    return render( request , "중랑구.html")
def 동작구( request ) :
    return render( request , "동작구.html")
def 노량진로( request ) :
    return render( request , "노량진로.html")