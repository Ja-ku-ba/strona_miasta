from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta():
        model = Account
        fields = ['email', 'username', 'password1', 'password2']

class UserLoginForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = ['email', 'password']

class ChangeUserData(UserCreationForm):
    class Meta():
        model = Account
        fields = ['email', 'username', 'password1', 'password2', 'hide_email', 'profile_image']
