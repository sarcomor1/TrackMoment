from django.db import models

class user(models.Model):
    id = models.BigAutoField(primary_key= True)
    email = models.EmailField()
    password = models.CharField(max_length= 225)
    page_slug = models.CharField(max_length= 225)
    is_active = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    last_login = models.DateTimeField()

class user(models.Model):
    integration_id = models.BigAutoField(primary_key= True)
    user_id = models.BigIntegerField()
    integration_type = models.enums()
    integration_details = models.JSONField()
    last_sync = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class user(models.Model):
    activity_id = models.BigAutoField(primary_key= True)
    user_id = models.BigIntegerField()
    activity_type = models.enums()
    activity_details = models.JSONField()
    image = models.JSONField()
    location = models.TextField()
    url = models.TextField()
    created_at = models.DateTimeField()
    activity_date = models.DateTimeField()