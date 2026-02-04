from django.core.exceptions import ValidationError


def validate_maintenance_cost(value):
    if value < 0:
        raise ValidationError('Maintenance costs cannot be negative')