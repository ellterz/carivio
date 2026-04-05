from django.contrib import admin
from maintenance.models import MaintenanceRecord

# Register your models here.

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ['car', 'date', 'cost', 'owner']
    list_filter = ['date']
    search_fields = ['car__name', 'description']