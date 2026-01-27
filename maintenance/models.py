from django.db import models
from cars.models import Car

# Create your models here.
class MaintenanceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='maintenance_records')
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


    class Meta:
        verbose_name = 'Maintenance Record'
        verbose_name_plural = 'Maintenance Records'
        ordering = ['-date']


    def __str__(self):
        return f'{self.car} - {self.description}'