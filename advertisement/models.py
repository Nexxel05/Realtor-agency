from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Realtor(AbstractUser):
    years_of_experience = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "realtor"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    def get_absolute_url(self):
        return reverse("advertisement:realtor-detail", kwargs={"pk": self.pk})


class Property(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "properties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("advertisement:property-detail", kwargs={"pk": self.pk})


class City(models.Model):
    name = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name="advertisements"
    )
    street = models.CharField(max_length=63)
    house = models.PositiveSmallIntegerField()
    apartment = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    total_area = models.PositiveSmallIntegerField(null=True, blank=True)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0, "Price can not be negative")]
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="advertisements"
    )
    realtors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="advertisements"
    )
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.city.name} - {self.street} {self.house}"

    def get_absolute_url(self):
        return reverse("advertisement:advertisement-detail", kwargs={"pk": self.pk})
