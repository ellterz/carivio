from django import forms

from parts.models import Part


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'car', 'price', 'manufacturer']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Oil Filters'
            }),
            'manufacturer': forms.TextInput(attrs={
                'placeholder': 'e.g. Bosch'
            }),
            'car': forms.CheckboxSelectMultiple(),
            'price': forms.NumberInput(attrs={
                'placeholder': 'e.g. 19.99'
            }),
        }
        help_texts = {
            'price': 'The price must be greater than or equal to zero.',
        }
        error_messages = {
            'name': {
                'required': 'Please enter the part name.',
            },
            'price': {
                'invalid': 'Please enter a valid number.',
                'required': 'Please enter the price.'
            },
            'manufacturer': {
                'required': 'Please enter the manufacturer.',
            }
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        return price
