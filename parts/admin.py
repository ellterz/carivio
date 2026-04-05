from django.contrib import admin
from parts.models import Part

# Register your models here.

@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'price', 'owner']
    list_filter = ['manufacturer']
    search_fields = ['name', 'manufacturer']