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


class RealtorUpdateForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = (
            "email",
            "years_of_experience",
            "phone_number"
        )


class RealtorSearchForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username, first name or last name..."})
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

    def clean_price(self):
        return validate_advertisement_price(
            self.cleaned_data["price"],
        )

    def clean_house(self):
        return validate_advertisement_house(
            self.cleaned_data["house"],
        )


def validate_advertisement_price(price):
    if price <= 0:
        raise ValidationError("Price must be higher then 0")
    return price


def validate_advertisement_house(house):
    if house <= 0:
        raise ValidationError("House number can not be negative")
    return house


class AdvertisementSearchForm(forms.ModelForm):
    cities = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label=""
    )

    class Meta:
        model = Advertisement
        fields = ("cities",)
