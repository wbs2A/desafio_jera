from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Formato: 01/01/2010')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birth_date', 'password1', 'password2',)