from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from advertisement.models import Realtor, Advertisement, City


class RealtorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Realtor
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "years_of_experience",
            "phone_number"
        )

    def clean_phone_number(self):
        return validate_realtor_phone_number(self.cleaned_data["phone_number"])


class RealtorUpdateForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = (
            "email",
            "years_of_experience",
            "phone_number"
        )

    def clean_phone_number(self):
        return validate_realtor_phone_number(self.cleaned_data["phone_number"])


def validate_realtor_phone_number(phone_number: str):
    if len(phone_number) != 9:
        raise ValidationError(
            "Phone number must be 9 digits long"
        )
    elif not phone_number.isdigit():
        raise ValidationError(
            "Phone number must contain only digits"
        )
    return phone_number


class RealtorSearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Search by username, first name or last name..."
        })
    )


class AdvertisementCreationForm(forms.ModelForm):
    realtors = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Advertisement
        fields = (
            "city",
            "street",
            "house",
            "apartment",
            "description",
            "total_area",
            "price",
            "property",
            "realtors"
        )


class AdvertisementSearchForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=""
    )

    class Meta:
        model = Advertisement
        fields = ("cities",)
