from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    page_slug = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
