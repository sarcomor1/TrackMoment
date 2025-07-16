from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class CustomUserCreationFormProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')
