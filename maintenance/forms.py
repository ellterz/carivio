from datetime import date

from django import forms

from maintenance.models import MaintenanceRecord


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['car', 'date', 'description', 'cost']
        widgets = {
            'car': forms.Select(),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Description of the maintenance work.'
            }),
            'cost': forms.NumberInput(attrs={
                'placeholder': 'e.g. 211.00',
            }),
        }
        help_texts = {
            'cost': 'The cost of the maintenance.',
        }

        error_messages = {
            'cost': {
                'invalid' : 'Enter a valid cost.',
                'required': 'Please enter the cost of the maintenance.'
            },
            'date': {
                'invalid' : 'Enter a valid date.',
                'required': 'Please enter the date of maintenance.',
            },
            'description': {
                'required': 'Enter a description of the maintenance work.'
            }
        }

    def clean_cost(self):
        cost = self.cleaned_data.get('cost')
        if cost is not None and cost < 0:
            raise forms.ValidationError('Maintenance cost cannot be negative.')
        return cost

    def clean_date(self):
        maintenance_date = self.cleaned_data.get('date')
        if maintenance_date and maintenance_date > date.today():
            raise forms.ValidationError('Maintenance date cannot be in the future.')
        return maintenance_date