from django.contrib.auth.models import User
from django import forms

#inherit from form object and create custom form
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    #meta data and fields of the class
    class Meta:
        model=User
        fields=['username','phone_number','email','user_image','password']