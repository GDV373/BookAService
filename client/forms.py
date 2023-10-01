from django import forms
from accounts.models import Car, Customer


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['Brand', 'Model', 'Fuel_Type', 'VIN', 'NumPlate']

    # helper = FormHelper()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['Fuel_Type'].widget = forms.Select(choices=Car.FUEL_TYPE_CHOICES)


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['Brand', 'Model', 'Fuel_Type', 'VIN', 'NumPlate']

    # Add Bootstrap classes to form fields
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['Location', 'Mobile', 'Vat_Number', 'ID_number', 'Address']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
