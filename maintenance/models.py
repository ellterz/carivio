from django.core.validators import MinValueValidator
from django.db import models
from cars.models import Car
from maintenance.validators import validate_maintenance_cost


# Create your models here.
class MaintenanceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance_records')
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_maintenance_cost],
    )


    class Meta:
        verbose_name = 'Maintenance Record'
        verbose_name_plural = 'Maintenance Records'
        ordering = ['-date']


    def __str__(self):
        return f'{self.car} - {self.description}'

    def formatted_cost(self):
        return f"{self.cost:.2f}"