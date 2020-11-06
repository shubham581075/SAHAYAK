from django.contrib import admin
from .models import User,ContactUser,UserService
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','user_name','first_name','last_name','email','mobile','home_address','address','password')

@admin.register(ContactUser)
class ContactUserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','address','description')


@admin.register(UserService)
class UserServiceAdmin(admin.ModelAdmin):
    list_display=('id','name','img','categ')