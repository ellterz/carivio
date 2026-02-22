from django import forms
from django.forms import MultipleChoiceField

from cars.models import Car, Manufacturer, Category


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'manufacturer', 'category', 'year', 'vin']
        labels = {
            'vin': 'Vehicle Identification Number',
            'name': 'Car name',
            'manufacturer': 'Manufacturer',
            'category': 'Category',
            'year': 'Year of Manufacture',
        }
        help_texts = {
            'category': 'Select one or more categories. To create a new category click "+Add Category".',
            'vin': '17 characters only',
            'year': 'Enter the car year.',
        }
        widgets = {
            'vin': forms.TextInput(attrs={
                'placeholder': 'e.g. WDB12345678901234',
            }),
            'year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 2021',
            }),
            'category': forms.SelectMultiple(),
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




class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['name', 'country']
        labels = {
            'name': 'Manufacturer Name',
            'country': 'Country',
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']