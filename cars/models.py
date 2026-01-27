from django.db import models

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
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True)


    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.year}"


    def age(self):
        from datetime import date
        return date.today().year - self.year
