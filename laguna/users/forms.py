from django import forms
from django.forms.widgets import DateInput
from .models import CustomUser, Address
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(forms.ModelForm):
    """Formularz rejestracji użytkownika"""

    password = forms.CharField(label="Hasło", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        widgets = {
            "birthday": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={
                    "firstDay": 1,
                    "pattern=": "\d{4}-\d{2}-\d{2}",
                    "lang": "pl",
                    "format": "yyyy-mm-dd",
                    "type": "date",
                },
            ),
            "phone_number": PhoneNumberPrefixWidget(initial="PL"),
            "cellphone_number": PhoneNumberPrefixWidget(initial="PL"),
        }
        fields = (
            "email",
            "username",
            "phone_number",
            "cellphone_number",
            "first_name",
            "last_name",
            "site",
            "birthday",
            "nationality",
            "place_of_birth",
        )

    """Sprawdzenie czy hasła się zgadzają"""

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Hasła nie są identyczne")
        return cd["password2"]

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get("email")

        # Check to see if any users already exist with this email as a username.
        try:
            match = CustomUser.objects.get(email=email.lower())
        except CustomUser.DoesNotExist:
            # Unable to find a user, this is fine
            return email

        # A user was found with this as a username, raise an error.
        raise forms.ValidationError("This email address is already in use.")


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["fullAddress", "address1", "address2", "zip_code", "city", "country"]
        labels = {
            "fullAddress": "Full Address",
            "address1": "Street Address",
            "address2": "Appartement Address",
        }
