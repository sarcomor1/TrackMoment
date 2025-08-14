from django.db import models
from django.conf import settings


INTEGRATION_CHOICES = [
    ('1', 'nothing')
]

class Integration(models.Model):
    integration_id = models.BigAutoField(primary_key= True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    integration_typ = models.CharField(max_length= 20, choices= INTEGRATION_CHOICES)
    integration_details = models.JSONField(null= True, blank= True)
    last_sync = models.DateField()
    create_at =  models.DateField(auto_now_add= True)
    update_at = models.DateField(auto_now= True)