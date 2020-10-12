from django.forms import ModelForm, PasswordInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }




# class ContactForm(forms.Form):
#     name= forms.CharField(max_length=500, label="Name")
#     email= forms.EmailField(max_length=500, label="Email")
#     comment= forms.CharField(label='',widget=forms.Textarea(
#                         attrs={'placeholder': 'Enter your comment here'}))