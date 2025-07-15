from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=225)
    page_slug = models.CharField(max_length=225)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_login = models.DateTimeField()
    integration = models.ForeignKey('integration.integration', on_delete=models.CASCADE)
    activity = models.ForeignKey('activity.activity', on_delete=models.CASCADE)
