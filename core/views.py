from django.shortcuts import render,HttpResponseRedirect
from .forms import User,Userprofile,Userlogin,Usercontact,Submitservice
from django.contrib.auth.models import User as django_user
from .models import User as t_user
from .models import ContactUser,UserService
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import time,webbrowser,pyautogui


def sendmsg(request):
    phone="+919565234221"
    msg="I am Shubham Singh"
    webbrowser.open('https://web.whatsapp.com/send?phone='+phone+'&text='+msg)
    time.sleep(10)
    pyautogui.press('enter')
    return HttpResponseRedirect('/')


def submitservice(request,serv,submit_serv):
    obj1=t_user.objects.all()
    obj2=t_user.objects.get(pk=1)
    for usr in obj1:
        if(str(usr.user_name)==str(request.user)):
            obj2=usr
            break
    
    fm=Submitservice({'name':obj2.first_name+" "+obj2.last_name, 'email':obj2.email, 'contact_no':obj2.mobile, 'address':obj2.home_address, 'service':serv+" "+submit_serv})
    return render(request,'serviceform.htm',{'form':fm})


def home(request):
    return render(request,'home.htm')
    

def register(request):
    if(request.method=='POST'):
        fm=User(request.POST)
        if(fm.is_valid()):
            user_name=fm.cleaned_data['user_name']
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email'] 
            home_address=fm.cleaned_data['home_address']
            address=fm.cleaned_data['address']
            password=fm.cleaned_data['password']
            re_password=fm.cleaned_data['re_password']
            if(password==re_password):
                fm=User()
            obj2=django_user(username=user_name,email=email,first_name=first_name,last_name=last_name,password=password)
            obj2.save()
            obj1=t_user(user_name=user_name,first_name=first_name,last_name=last_name,email=email,mobile=user_name,home_address=home_address,address=address,password=password)
            obj1.save()
            messages.success(request,"Registration Completed !!")
    else:
        fm=User()

    dict1={'form':fm}
    return render(request,'signup.htm',dict1)



def signin(request):
    if(request.method=='POST'):
        fm=Userlogin(request=request,data=request.POST)
        if(fm.is_valid()):
            user=authenticate(username=fm.cleaned_data['username'],password=fm.cleaned_data['password'])
            if(user is not None):
                login(request,user)
                messages.success(request,"Logged in Successfully !")
                return HttpResponseRedirect('/')
            else:
                messages.warning(request,'username and/or password is/are wrong')
    else:
        fm=Userlogin()

    dict1 = {'form':fm}
    return render(request,'login.htm',dict1)



def profile(request):
    if(request.method=="POST"):
        fm=Userprofile(request.POST,instance=request.user)
        if(fm.is_valid()):
            messages.success(request,"Profile Updated")
            fm.save()   
    fm=Userprofile(instance=request.user)
    return render(request,'profile.htm',{'form':fm})



def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')


def contact(request):
    if(request.method=="POST"):
        fm=Usercontact(request.POST)
        if(fm.is_valid()):
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            mob=fm.cleaned_data['phone_no']
            add=fm.cleaned_data['address']
            des=fm.cleaned_data['desc']
            obj1=ContactUser(name=nm,email=em,mobile=mob,address=add,description=des)
            obj1.save()
            messages.info(request,"Your Query has been submitted and it will be resolved soon !")
    fm=Usercontact()
    return render(request,'contact.htm',{'form':fm})


def userservice(request,serv):
    obj1=UserService.objects.all()
    #print(obj1)
    #print(serv)
    #return HttpResponseRedirect('/')
    return render(request,'services.htm',{'dict1':obj1,'servi':serv})

