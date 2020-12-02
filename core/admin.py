from django.contrib import admin
from .models import User,ContactUser,UserService,ServiceProvider,BookedServices
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','email','mobile','address','password','categ')

@admin.register(ContactUser)
class ContactUserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','address','description')


@admin.register(UserService)
class UserServiceAdmin(admin.ModelAdmin):
    list_display=('id','name','img','categ','description')


@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','address','categ')

@admin.register(BookedServices)
class BookedServicesAdmin(admin.ModelAdmin):
    list_display=('id','required_service','booking_date','booking_time','expected_date','expected_time','total_charge','extra_charge','vendor','requestor')