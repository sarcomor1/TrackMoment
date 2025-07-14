from django.db import models
from enum import Enum

class EnumIntegration(Enum):
    LIBRARY = 'football'

class EnumActivety(Enum):
    SHOPPING = 'shopping'


class User(models.Model):
    id = models.BigAutoField(primary_key= True)
    email = models.EmailField()
    password = models.CharField(max_length= 225)
    page_slug = models.CharField(max_length= 225)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_login = models.DateTimeField()
    integration = models.ForeignKey('integration', on_delete= models.CASCADE)
    activity = models.ForeignKey('activity', on_delete= models.CASCADE)
    

class Integration(models.Model):
    integration_id = models.BigAutoField(primary_key= True)
    user_id = models.BigIntegerField()
    integration_type = models.CharField(max_length= 20, choices=[(tag.value, tag.name) for tag in EnumIntegration])
    integration_details = models.JSONField()
    last_sync = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Activity(models.Model):
    activity_id = models.BigAutoField(primary_key= True)
    user_id = models.BigIntegerField()
    activity_type = models.CharField(max_length= 20, choices=[(tag.value, tag.name) for tag in EnumActivety])
    activity_details = models.JSONField()
    image = models.JSONField()
    location = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField()
    activity_date = models.DateTimeField()
