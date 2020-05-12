from django import forms
from django.contrib.auth.models import User
from siteapp.models import UserProfileInfoModel

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        fields = ('username', 'email', 'password')
        model = User

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfoModel
        fields = ('portfolio_site', 'profile_pics')
