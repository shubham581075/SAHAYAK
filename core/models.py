from django.db import models

class User(models.Model):
    user_name=models.CharField(max_length=70)
    first_name=models.CharField(max_length=70,default="singh")
    last_name=models.CharField(max_length=70,default="singh")
    email=models.EmailField(max_length=70)
    mobile=models.CharField(max_length=70)
    home_address=models.TextField()
    address=models.TextField()
    password=models.CharField(max_length=50)

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
    

