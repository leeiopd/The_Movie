from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile

class CreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = get_user_model()
        fields = ['username', ]


class LoginForm(forms.ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
     
        
# class ChangeForm(UserChangeForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['password', 'nickname', 'introduction']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'point',)