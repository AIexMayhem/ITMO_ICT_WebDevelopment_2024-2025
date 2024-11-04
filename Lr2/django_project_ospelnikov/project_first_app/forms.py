from django import forms
from .models import Owner


# creating a form
class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = [
            "first_name",
            "last_name",
            "birth_date"
        ]