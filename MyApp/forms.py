from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Comment


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


# class ContactForm(forms.Form):
#     name= forms.CharField(max_length=500, label="Name")
#     email= forms.EmailField(max_length=500, label="Email")
#     comment= forms.CharField(label='',widget=forms.Textarea(
#                         attrs={'placeholder': 'Enter your comment here'}))