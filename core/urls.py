from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('<city>/',views.home,name='Home'),
    path('<city>/register/',views.register,name='Register'),
    path('<city>/login/',views.signin,name='Login'),
    path('<city>/logout/',views.userlogout,name='Logout'),
    path('<city>/profile/',views.profile,name='Profile'),
    path('<city>/contact/',views.contact,name='Contact'),
    path('<city>/services/<serv>/',views.userservice,name='Userservice'),
    path('<city>/services/<serv>/<submit_serv>/',views.submitservice,name='Submitservice'),
    path('sendmsg/',views.sendmsg,name='Sendmsg'),
    path('<city>/search/',views.search,name='Search'),
    path('searchservice',views.searchservice,name='Searchservice')
    #path('autocomplet/',views.autocomplet,name=autocomplet)
]