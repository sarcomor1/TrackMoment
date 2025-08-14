from django import forms
from .models import ActivityModels


class ActivityForms(forms.ModelForm):
    class Meta:
        model = ActivityModels
        fields = ['activity_type', 'activity_details', 'location', 'activity_date', 'url', 'image']
