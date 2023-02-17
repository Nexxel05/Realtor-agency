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


class City(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="advertisements")
    street = models.CharField(max_length=63)
    house = models.IntegerField()
    apartment = models.CharField(max_length=63, null=True, blank=True)
    description = models.TextField(blank=True)
    total_area = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="advertisements")
    realtors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="advertisements")
    sold = models.BooleanField()

    def __str__(self):
        return f"{self.city.name} - {self.street} {self.house}/{self.apartment}"
