from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=70,default="singh")
    last_name=models.CharField(max_length=70,default="singh")
    email=models.EmailField(max_length=70)
    mobile=models.CharField(max_length=70)
    address=models.TextField()
    password=models.CharField(max_length=50)
    categ=models.CharField(max_length=2,default='0')

class ContactUser(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    mobile=models.CharField(max_length=10)
    address=models.TextField(max_length=150)
    description=models.TextField()

class UserService(models.Model):
    name=models.CharField(max_length=70)
    img=models.ImageField()
    categ=models.CharField(max_length=70)
    price=models.IntegerField(default=100)
    description=models.CharField(max_length=1000,default="dfgdfg")

class ServiceProvider(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    mobile=models.CharField(max_length=10)
    address=models.TextField(max_length=150)
    categ=models.CharField(max_length=70)

class BookedServices(models.Model):
    required_service=models.CharField(max_length=70)
    booking_date=models.DateField()
    booking_time=models.TimeField()
    expected_date=models.DateField()
    expected_time=models.TimeField()
    total_charge=models.CharField(max_length=70)
    extra_charge=models.CharField(max_length=70)
    vendor = models.CharField(max_length=15)
    requestor = models.CharField(max_length=15)
    
    

