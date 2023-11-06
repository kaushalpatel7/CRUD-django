from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

from django import forms

from django.contrib.auth.forms import AuthenticationForm

from django.forms.widgets import PasswordInput , TextInput

from .models import Record
# register or create a user

class CreateUserform(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username','password1','password2']
        
        
# login a user form

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    
    password = forms.CharField(widget=PasswordInput())
    


# Create a record
class CreateRecordForm(forms.ModelForm):
    class Meta:
        
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']
    
    
# Create a record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        
        model = Record
        fields = ['first_name','last_name','email','phone','address','city','province','country']
    
    


