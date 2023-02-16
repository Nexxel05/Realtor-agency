from django.urls import path

from advertisement.views import (
    index,
    RealtorListView,
    RealtorDetailView,
    PropertyListView,
    PropertyDetailView,
    AdvertisementListView,
    AdvertisementDetailView
)

urlpatterns = [
    path('', index, name="index"),
    path('realtors/', RealtorListView.as_view(), name="realtor-list"),
    path('realtors/<int:pk>', RealtorDetailView.as_view(), name="realtor-detail"),
    path('properties/', PropertyListView.as_view(), name="property-list"),
    path('properties/<int:pk>', PropertyDetailView.as_view(), name="property-detail"),
    path('advertisements/', AdvertisementListView.as_view(), name="advertisement-list"),
    path('advertisements/<int:pk>', AdvertisementDetailView.as_view(), name="advertisement-detail"),

]

app_name = "advertisement"
