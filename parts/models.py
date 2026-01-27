from django.db import models
from cars.models import Car

# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=100)
    car = models.ManyToManyField(Car, related_name='parts')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    manufacturer = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        return self.name