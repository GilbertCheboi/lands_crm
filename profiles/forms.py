from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelChoiceField

User = get_user_model()

from .models import Profile
class UserProfileForm(forms.ModelForm):
   
    bio = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    class Meta:
        model = Profile
        fields = [ 
            "user",
            "first_name",
            "last_name",
            "email",
            "image",
            "bio",
            "followers",
            
            ]


class ProfileBasicForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email_address = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    bio = forms.CharField(required=False)

