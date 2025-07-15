from django.db import models
from enum import Enum

class EnumActivety(Enum):
    SHOPPING = 'shopping'

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