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