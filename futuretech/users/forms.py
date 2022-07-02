from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import RegisteredUser

class RegistrationForm(forms.ModelForm):  
    class Meta:
        model = RegisteredUser
        fields = ("first_name", "middle_name", "last_name", 
                    "birth_date", "gender", "email",
                    "phone_number", "courses")


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1",
                "password2"]