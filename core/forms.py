from django import forms
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User as user_admin
from django.utils.translation import gettext,gettext_lazy as _

class User(forms.Form):
    mobile_no=forms.CharField(label='Mobile_no',widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Re-Enter Password")

    def clean(self):
        cleaned_data=super().clean()
        pass1=self.cleaned_data['password']
        pass2=self.cleaned_data['re_password']
        if(pass1!=pass2):
            raise forms.ValidationError('Password not matched')


class Userprofile(UserChangeForm):
    password=None
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label="Phone no")
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model=user_admin
        fields=['first_name','last_name','username','email']


class Userlogin(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password=forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
        

class Usercontact(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    desc=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))


class Submitservice(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    contact_no=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    service=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    expected_date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}), required=False)
    expected_time=forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type':'time'}), required= False)
    problem_desc=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':5}))


class Search(forms.Form):
    service=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mr-sm-2','placeholder':'Search Services','id':'service','aria-label':'Search'}))