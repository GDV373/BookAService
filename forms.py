from django import forms


class RegistrationForm(forms.Form):
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    email = forms.EmailField()
    location = forms.ChoiceField(
        choices=[(1, 'Location 1'), (2, 'Location 2')])
    address = forms.CharField(max_length=255)
    vat = forms.CharField(max_length=255, required=False)
    number = forms.CharField(max_length=8)
    id_number = forms.CharField(max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
