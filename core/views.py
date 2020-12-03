from django.shortcuts import render,HttpResponseRedirect
from .forms import User,Userprofile,Userlogin,Usercontact,Submitservice,Search,completeservice
from django.contrib.auth.models import User as django_user
from .models import User as t_user
from .models import ContactUser,UserService,ServiceProvider,BookedServices
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from geopy.distance import great_circle
from opencage.geocoder import OpenCageGeocode
from twilio.rest import Client
import datetime as dt
from django.http import JsonResponse
import string,random



def faq(request,city):
    return render(request,'faq.htm',{'place':city})


def search(request,city):
    if(request.method=="POST"):
        fm2=Search(request.POST)
        if(fm2.is_valid()):
            servic=fm2.cleaned_data['service']
            obj1=UserService.objects.get(name=servic)
            urlreq='/'+city+'/services/'+str(obj1.categ)+'/'+servic+'/'
            return HttpResponseRedirect(urlreq)

def sendmsg(msg, recipient_no):
     
    client = Client(account_sid, auth_token) 
    message = client.messages.create(from_='+19034965809',  body=msg, to=recipient_no)



def calculate_dis(source,destination):
    key = '14746e952d8a48e3abfb96ec0b7c035f'
    geocoder = OpenCageGeocode(key)
    query = source
    results = geocoder.geocode(query)
    source_lat = results[0]['geometry']['lat']
    source_long = results[0]['geometry']['lng']
    query = destination
    results = geocoder.geocode(query)
    destination_lat = results[0]['geometry']['lat']
    destination_long = results[0]['geometry']['lng']
    source1 = (source_lat, source_long) 
    destination1 = (destination_lat, destination_long)
    distanc = great_circle(source1, destination1).km
    return distanc
    





def submitservice(request,serv,submit_serv,city):
    fm2=Search()
    if(request.method=="POST"):
        fm=Submitservice(request.POST)
        if(fm.is_valid()):
            source=fm.cleaned_data['address']
            key = '14746e952d8a48e3abfb96ec0b7c035f'
            Vendors=ServiceProvider.objects.all()
            mini=99999999
            identifier=-1
            listofvendors=[]
            for provider in Vendors:
                if(provider.categ==serv):
                    listofvendors.append(provider)

            def myfun(provider):
                return calculate_dis(source, provider.address)

            service_provider='dvf'
            listofvendors.sort(key=myfun)
            for provider in listofvendors:
                services=BookedServices.objects.filter(vendor=provider.mobile, expected_date=fm.cleaned_data['expected_date'], expected_time__lte=(dt.datetime.combine(dt.date(1,1,1),fm.cleaned_data['expected_time'])+dt.timedelta(hours=1)).time(), expected_time__gte=(dt.datetime.combine(dt.date(10,10,10),fm.cleaned_data['expected_time'])-dt.timedelta(hours=1)).time())
                if(len(services)==0):
                    service=UserService.objects.get(name=submit_serv)
                    service_provider=provider.mobile
                    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 15))
                    obj3=BookedServices(required_service=serv+' '+submit_serv,booking_date=(dt.datetime.now()).date(),booking_time=(dt.datetime.now()).time(),expected_date=fm.cleaned_data['expected_date'],expected_time=fm.cleaned_data['expected_time'],total_charge=service.price,extra_charge=str(0),vendor=service_provider,requestor=request.user,status='Booked',token=res)
                    obj3.save()
                    #if(service.expected_date==fm.cleaned_data[date] and int(service.expected_time)fm.cleaned_data[])
                    
            msg = 'Contact asap !!!                 '+'Name : '+fm.cleaned_data['name']+'              '+'Phone no : '+fm.cleaned_data['contact_no']+'       '+'Address : '+fm.cleaned_data['address']+'        '+'Service Required : '+fm.cleaned_data['service']+'       '+'Expected Date, Time : '+str(fm.cleaned_data['expected_date'])+' '+str(fm.cleaned_data['expected_time'])+'       '+'Description : '+fm.cleaned_data['problem_desc']
            recipient='+91'+str(service_provider)
            print(recipient)
            sendmsg(msg,recipient)
            messages.success(request,'Service Booked!!!')

    else:
        #obj1=t_user.objects.all()
        obj2=t_user.objects.get(mobile=request.user)
        fm=Submitservice({'name':obj2.first_name+" "+obj2.last_name, 'email':obj2.email, 'contact_no':obj2.mobile, 'address':obj2.address, 'service':serv+" "+submit_serv})
    obj3=UserService.objects.get(name=submit_serv)
    pric=obj3.price
    ls=[]
    s=str(obj3.description)
    i=0
    while(i<len(s)):
        flag=0
        while(s[i]!='*'):
            if(flag==0):
                flag=1
                s1=s[i]
            else:
                s1=s1+s[i]
            i=i+1
            if(i>=(len(s)-1)):
                break
            if(s[i]=='*'):
                i=i+1
                break
        ls.append(s1)
        if(i>=len(s)):
            break
    ls.pop()
    ls.pop()
    imag=obj3.img.url
    return render(request,'serviceform.htm',{'form':fm,'form2':fm2,'place':city,'desc':ls,'img':imag,'price':pric})


def home(request,city):
    fm2=Search()
    return render(request,'home.htm',{'form2':fm2,'place':city})
    

def register(request,city):
    fm2=Search()
    if(request.method=='POST'):
        fm=User(request.POST)
        if(fm.is_valid()):
            mobile=fm.cleaned_data['mobile_no']
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email'] 
            address=fm.cleaned_data['address']
            password=fm.cleaned_data['password']
            re_password=fm.cleaned_data['re_password']
            if(password==re_password):
                fm=User()
            obj2=django_user(username=mobile,email=email,first_name=first_name,last_name=last_name,password=password)
            obj2.save()
            obj1=t_user(mobile=mobile,first_name=first_name,last_name=last_name,email=email,address=address,password=password,categ='0')
            obj1.save()
            messages.success(request,"Registration Completed !!")
            return HttpResponseRedirect('/'+city+'/login/')
    else:
        fm=User()

    dict1={'form':fm,'form2':fm2,'place':city}
    return render(request,'signup.htm',dict1)



def signin(request,city):
    fm2=Search()
    if(request.method=='POST'):
        fm=Userlogin(request=request,data=request.POST)
        if(fm.is_valid()):
            user=authenticate(username=fm.cleaned_data['username'],password=fm.cleaned_data['password'])
            if(user is not None):
                login(request,user)
                messages.success(request,"Logged in Successfully !")
                return HttpResponseRedirect('/'+city+'/')
            else:
                messages.warning(request,'username and/or password is/are wrong')
    else:
        fm=Userlogin()

    dict1 = {'form':fm,'form2':fm2,'place':city}
    return render(request,'login.htm',dict1)


def profile(request,city):
    fm2=Search()
    if(request.method=="POST"):
        fm=User(request.POST)
        if(fm.is_valid()):
            mobile=fm.cleaned_data['mobile_no']
            first_name=fm.cleaned_data['first_name']
            last_name=fm.cleaned_data['last_name']
            email=fm.cleaned_data['email'] 
            address=fm.cleaned_data['address']
            password=fm.cleaned_data['password']
            re_password=fm.cleaned_data['re_password']
            pk1=(t_user.objects.get(mobile=str(request.user))).id
            pk2=(django_user.objects.get(username=str(request.user))).id
            if(password==re_password):
                fm=User()
            obj1=t_user(id=pk1, first_name=first_name,last_name=last_name,email=email,mobile=mobile,address=address,password=password)
            #obj1.set_password(password)
            obj1.save()
            obj2=django_user(id=pk2,username=mobile,email=email,first_name=first_name,last_name=last_name)
            obj2.set_password(password)
            obj2.save()
            logout(request)
            #update_session_auth_hash(request,mobile)
            messages.success(request,"Profile Updated...login again")
            return HttpResponseRedirect('/'+city+'/login/')
        
    customer=t_user.objects.get(mobile=request.user)
    if(customer.categ=='0'):
        obj4=BookedServices.objects.filter(requestor=request.user)
        
    else:
        obj4=BookedServices.objects.filter(vendor=request.user)
        
    fm3=completeservice()
    fm=User({'mobile_no':customer.mobile, 'first_name':customer.first_name, 'last_name':customer.last_name, 'email':customer.email, 'address':customer.address,'password':customer.password, 're_password':customer.password})
    return render(request,'profile3.htm',{'form':fm,'servicelist':obj4,'form2':fm2,'place':city,'usr':customer,'form3':fm3})


def searchservice(request):
    if 'term' in request.GET:
        qs=UserService.objects.filter(name__contains=request.GET.get('term'))
        titles=list()
        for service in qs:
            titles.append(service.name)
        return JsonResponse(titles, safe=False)




def userlogout(request,city):
    logout(request)
    return HttpResponseRedirect('/'+city+'/')


def contact(request,city):
    fm2=Search()
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
    return render(request,'contact.htm',{'form':fm,'form2':fm2,'place':city})


def userservice(request,serv,city):
    if(request.user.is_authenticated):
        fm2=Search()
        obj1=UserService.objects.all()
        #print(obj1)
        #print(serv)
        #return HttpResponseRedirect('/')
        return render(request,'services.htm',{'dict1':obj1,'servi':serv,'form2':fm2,'place':city})
    else:
        messages.info(request,"Login first !!")
        return HttpResponseRedirect('/'+city+'/')

def cancelservice(request,ide,city):
    obj1=BookedServices.objects.get(id=ide)
    str1=obj1.required_service
    obj1.delete()
    messages.info(request,str1+' Service Cancelled')
    return HttpResponseRedirect('/'+city+'/profile/')


def completeserve(request,city,ide):
    fm=completeservice(request.POST)
    if(fm.is_valid()):
        token=fm.cleaned_data['token']
        obj2=BookedServices.objects.get(id=ide)
        obj2.status="Delivered"
        obj2.save()
        messages.success(request,"Service Delivered")
        return HttpResponseRedirect('/'+city+'/profile/')