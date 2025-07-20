from django.db import models
from django.conf import settings
from datetime import date


ACTIVITY_CHOICES = [
    ('Playing', 'Playing'),
    ('TV', 'TV'),
    ('Shopping', 'Shopping'),
]

class Activity(models.Model):
    activity_id =models.BigAutoField(primary_key= True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES)
    activity_details = models.JSONField(null=True, blank=True)
    image = models.ImageField(upload_to= 'photo/%Y/%m/%d')
    location = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    create_at =  models.DateField(default=date.today)
    activity_date = models.DateTimeField()