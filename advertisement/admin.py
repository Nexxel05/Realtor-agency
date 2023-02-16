from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from advertisement.models import Realtor, Advertisement, Address, Property


@admin.register(Realtor)
class RealtorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience", "phone_number", "date_registered")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience", "phone_number")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("years_of_experience", "phone_number")},)
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "street", "house", "apartment", "zip_code")
    search_fields = ("city",)
    list_filter = ("city",)


admin.site.register(Property)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("address", "description", "total_area", "price", "property", "sold")
    search_fields = ("address__street",)
    list_filter = ("property__name",)
