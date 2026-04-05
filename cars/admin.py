from django.contrib import admin
from cars.models import Car, Manufacturer, Category

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'year', 'owner']
    list_filter = ['manufacturer', 'year']
    search_fields = ['name', 'vin']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']