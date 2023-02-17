from django.urls import path

from advertisement.views import (
    index,
    RealtorListView,
    RealtorDetailView,
    PropertyListView,
    PropertyDetailView,
    AdvertisementListView,
    AdvertisementDetailView,
    PropertyCreateView,
    PropertyDeleteView,
    RealtorCreateView
)

urlpatterns = [
    path('', index, name="index"),
    path('realtors/', RealtorListView.as_view(), name="realtor-list"),
    path('realtors/<int:pk>/', RealtorDetailView.as_view(), name="realtor-detail"),
    path('realtors/create/', RealtorCreateView.as_view(), name="realtor-create"),

    path('properties/', PropertyListView.as_view(), name="property-list"),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name="property-detail"),
    path('properties/create/', PropertyCreateView.as_view(), name="property-create"),
    path('properties/delete/<int:pk>/', PropertyDeleteView.as_view(), name="property-delete"),

    path('advertisements/', AdvertisementListView.as_view(), name="advertisement-list"),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement-detail"),

]

app_name = "advertisement"
