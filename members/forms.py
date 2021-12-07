from django.contrib.auth.models import User
from django import forms


class RegistrationForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('username','email','password')
        widgets= {
            'password': forms.PasswordInput()
        }

       