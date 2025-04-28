from django import forms
from django.forms import ModelForm
from .models import User
from django.utils.translation import gettext_lazy as _
from .models import User

class SignupForm(ModelForm):
    class Meta: 
        model = User
        fields = ['email', 'username', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'signup-form--input', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'signup-form--input', 'placeholder': 'Name'}),
            'password': forms.PasswordInput(attrs={'class': 'signup-form--input', 'placeholder':'Password'})
        }
    

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User already exists with the given email!')
        return email


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(attrs={'class': 'signup-form--input', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={'class': 'signup-form--input', 'placeholder':'Password'}))
        