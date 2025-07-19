from django.db import models
from django.conf import settings


class Activity(models.Model):
    activity_id =models.BigAutoField(primary_key= True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length= 255)
