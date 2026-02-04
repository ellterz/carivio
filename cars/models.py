from django.db import models
from cars.validators import validate_car_year, validate_car_vin
from datetime import date

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"
        ordering = ['name']


    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Car(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    category = models.ManyToManyField(Category, related_name='cars')
    year = models.PositiveIntegerField(
        validators=[validate_car_year]
    )
    vin = models.CharField(
        max_length=17,
        unique=True,
        validators=[validate_car_vin]
    )


    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.manufacturer} {self.year}"


    def age(self):
        return date.today().year - self.year

    def total_maintenance_cost(self):
        return sum(record.cost for record in self.maintenance_records.all())

    def save(self, *args, **kwargs):
        self.vin = self.vin.strip().upper()
        super().save(*args, **kwargs)