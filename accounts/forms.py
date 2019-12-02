from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: DD-MM-YYYY')

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'birth_date', 'password1', 'password2',)