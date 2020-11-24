from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('register/',views.register,name='Register'),
    path('login/',views.signin,name='Login'),
    path('logout/',views.userlogout,name='Logout'),
    path('profile/',views.profile,name='Profile'),
    path('contact/',views.contact,name='Contact'),
    path('services/<serv>/',views.userservice,name='Userservice'),
    path('services/<serv>/<submit_serv>/',views.submitservice,name='Submitservice'),
    path('sendmsg/',views.sendmsg,name='Sendmsg'),
    path('search/',views.search,name='Search')
    #path('autocomplet/',views.autocomplet,name=autocomplet)
]