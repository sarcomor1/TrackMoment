from django.contrib import admin
from .models import Integration


@admin.register(Integration)
class IntegrationAdmin(admin.ModelAdmin):
    list_display = ['integration_id', 'user_id', 'integration_typ', 'integration_details', 'last_sync', 'create_at', 'update_at' ]
