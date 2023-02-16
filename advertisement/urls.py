from django.urls import path

from advertisement.views import index

urlpatterns = [
    path('', index, name="index"),
]

app_name = "advertisement"
