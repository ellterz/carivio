from django import forms

from maintenance.models import MaintenanceRecord


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        fields = ['date', 'description', 'cost']
        widgets = {
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

    def clean_cost(self):
        cost = self.cleaned_data('cost')
        if cost < 0:
            raise forms.ValidationError('Maintenance cost cannot be negative.')
        return cost