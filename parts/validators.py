from django.core.exceptions import ValidationError


def validate_part_price(value):
    if value < 0:
        raise ValidationError('Part price cannot be negative')