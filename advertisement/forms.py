from django.contrib.auth.forms import UserCreationForm

from advertisement.models import Realtor


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
