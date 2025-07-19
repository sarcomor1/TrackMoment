from django import forms
from django.contrib.auth import get_user_model
from .models import Activity

User = get_user_model()

class ActivityForms(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_id', 'user', 'location']
        