from django.contrib import admin
from .models import Activity

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'user_id', 'activity_type', 'activity_details', 'image', 'location', 'url', 'create_at', 'activity_date' )
