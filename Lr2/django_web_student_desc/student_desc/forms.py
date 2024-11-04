from django import forms
from .models import User


# creating a form
class RegisterForm(forms.ModelForm):
    class Meta:
        # specify model to be used
        model = User

        # specify fields to be used
        fields = [
            "position",
            "first_name",
            "last_name",
            "email",
            "birth_date",
        ]