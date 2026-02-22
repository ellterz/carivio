from django.db import models
from cars.models import Car
from parts.validators import validate_part_price


# Create your models here.
class Part(models.Model):
    name = models.CharField(max_length=100)
    car = models.ManyToManyField(Car, related_name='parts')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_part_price],
    )
    manufacturer = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        return f"{self.name} {self.price}"

    def formatted_price(self):
        return f"{self.price:.2f}"