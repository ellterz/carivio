from datetime import date

from django.core.exceptions import ValidationError

FIRST_CAR_YEAR = 1886

def validate_car_year(value):
    current_year = date.today().year

    if value > current_year:
        raise ValidationError('The year of the car cannot be in the future')

    if value < FIRST_CAR_YEAR:
        raise ValidationError(f"Sorry, the first car was created in {FIRST_CAR_YEAR}. Please enter a valid year.")


def validate_car_vin(value):

    if len(value.strip()) != 17:
        raise ValidationError(f"VIN must be exactly 17 characters long.")

    if not value.isalnum():
        raise ValidationError(f"VIN must contain only letters and numbers.")

    if any(char in {'I', 'O', 'Q'} for char in value.upper()):
        raise ValidationError(f"VIN cannot contains I, O, or Q characters.")