from django import forms

from cars.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'manufacturer', 'category', 'year', 'vin']
        labels = {
            'vin': 'Vehicle Identification Number',
            'car': 'Car name',
            'manufacturer': 'Manufacturer',
            'category': 'Category',
            'year': 'Year of Manufacture',
        }
        help_texts = {
            'vin': 'Exactly 17 characters.',
            'year': 'Enter the car year.',
        }
        widgets = {
            'vin': forms.TextInput(attrs={
                'placeholder': 'e.g. WDB12345678901234',
            }),
            'year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2021',
            })
        }
        error_messages = {
            'vin': {
                'required': 'This field is required.',
                'unique': 'This field is already in use.',
                'max_length': 'This field should be exactly 17 characters.',
            },
            'year': {
                'invalid': 'Enter a valid year.',
            },
            'name': {
                'required': 'Please enter the car name.',
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['vin'].disabled = True