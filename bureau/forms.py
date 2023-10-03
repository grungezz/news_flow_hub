from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from bureau.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    redactors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )

    def clean_years_of_experience(self):  # this logic is optional, but possible
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


class RedactorExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ["years_of_experience"]


class RedactorUpdateDataForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = ['username', 'first_name', 'last_name', 'email', 'years_of_experience']

    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'years_of_experience': forms.NumberInput(attrs={'class': 'form-control'}),
    }

    def clean_years_of_experience(self):
        return validate_years_of_experience(self.cleaned_data["years_of_experience"])


def validate_years_of_experience(years_of_experience):
    try:
        years_of_experience = int(years_of_experience)
        if not 0 <= years_of_experience <= 80:
            raise ValidationError("Please enter a valid number between 0 and 80")
    except ValueError:
        raise ValidationError("Years of experience should contain only numbers")

    return years_of_experience
