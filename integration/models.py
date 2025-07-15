from django.db import models
from enum import Enum

class EnumIntegration(Enum):
    LIBRARY = 'football'

class Integration(models.Model):
    integration_id = models.BigAutoField(primary_key= True)
    user_id = models.BigIntegerField()
    integration_type = models.CharField(max_length= 20, choices=[(tag.value, tag.name) for tag in EnumIntegration])
    integration_details = models.JSONField()
    last_sync = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()