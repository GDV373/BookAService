from django import forms
from django.core.validators import EmailValidator, RegexValidator
from django.core.exceptions import ValidationError


# Start Test Customer form
class CustomerRegistrationForm(forms.Form):
    fname = forms.CharField(max_length=255, required=True)
    lname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    location = forms.ChoiceField(
        choices=[(1, 'Location 1'), (2, 'Location 2')],
        required=True
    )
    address = forms.CharField(max_length=255, required=True)
    vat = forms.CharField(max_length=255,  required=False)
    number = forms.CharField(max_length=8, required=True)
    id_number = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

# End Test Customer form


# Start Test Business form
class BusinessRegistrationForm(forms.Form):
    fname = forms.CharField(max_length=255, required=True)
    lname = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(
        required=True,
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    location = forms.ChoiceField(
        choices=[(1, 'Location 1'), (2, 'Location 2')],
        required=True
    )
    address = forms.CharField(max_length=255, required=True)
    vat_pattern = r'^MT\d{4}-\d{4}$'
    vat_validator = RegexValidator(
        vat_pattern,
        message="VAT must follow the format MT1245-1245"
    )

    vat = forms.CharField(
        max_length=255,
        required=True,
        validators=[vat_validator]
    )
    businessname = forms.CharField(max_length=255, required=True)
    number = forms.CharField(max_length=8, required=True)
    id_number = forms.CharField(max_length=10, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")

# End Test Business form
