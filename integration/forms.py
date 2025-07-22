from django import forms
from django.contrib.auth import get_user_model
from models import Integration

User = get_user_model()

class _IntegrationForm(forms.ModelForm):
    class Meta:
        model = Integration
        fields = ['integration_id', 'user_id', 'integration_typ', 'integration_details', 'last_sync', 'create_at', 'update_at' ]
