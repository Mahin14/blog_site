from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_login.models import UserProfile

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email=forms.EmailField( required=True ,label='Email Address')
    class Meta:
        model =User
        fields=('first_name','last_name','username','email','password1','password2')


class UserProfileChange(UserChangeForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')


class ProfilePic(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['profile_pic']