from django.contrib.auth.models import AbstractUser
from django.db import models


class Realtor(AbstractUser):
    years_of_experience = models.IntegerField()

    class Meta:
        verbose_name = "realtor"

    def str(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Property(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=63)
    street = models.CharField(max_length=63)
    house = models.CharField(max_length=63)
    apartment = models.CharField(max_length=63)
    zip_code = models.IntegerField()

    class Meta:
        ordering = ["city"]
        verbose_name_plural = "addresses"


class Advertisement(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="advertisements")
    description = models.TextField()
    total_area = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="advertisements")
    realtors = models.ManyToManyField(Realtor, related_name="advertisements")
    sold = models.BooleanField()
