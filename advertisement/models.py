from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Realtor(AbstractUser):
    years_of_experience = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "realtor"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Property(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "properties"

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=63)
    street = models.CharField(max_length=63)
    house = models.IntegerField()
    apartment = models.CharField(max_length=63, null=True, blank=True)
    zip_code = models.IntegerField()

    class Meta:
        ordering = ["city"]
        verbose_name_plural = "addresses"

    @property
    def full_address(self):
        return f"{self.city} - {self.street} {self.house}/{self.apartment}"


class Advertisement(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="advertisements")
    description = models.TextField(blank=True)
    total_area = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="advertisements")
    realtors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="advertisements")
    sold = models.BooleanField()

    def __str__(self):
        return self.address.full_address
