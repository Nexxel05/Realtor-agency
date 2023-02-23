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
    RealtorCreateView,
    RealtorDeleteView,
    AdvertisementCreateView,
    AdvertisementDeleteView,
    AdvertisementUpdateView,
    RealtorUpdateView,
    PropertyUpdateView
)

urlpatterns = [
    path('', index, name="index"),

    path('realtors/', RealtorListView.as_view(), name="realtor-list"),
    path('realtors/<int:pk>/', RealtorDetailView.as_view(), name="realtor-detail"),
    path('realtors/create/', RealtorCreateView.as_view(), name="realtor-create"),
    path('realtors/<int:pk>/delete/', RealtorDeleteView.as_view(), name="realtor-delete"),
    path('realtors/<int:pk>/update/', RealtorUpdateView.as_view(), name="realtor-update"),

    path('properties/', PropertyListView.as_view(), name="property-list"),

    path('advertisements/', AdvertisementListView.as_view(), name="advertisement-list"),
    path('advertisements/<int:pk>/', AdvertisementDetailView.as_view(), name="advertisement-detail"),
    path('advertisements/create', AdvertisementCreateView.as_view(), name="advertisement-create"),
    path('advertisements/<int:pk>/delete/', AdvertisementDeleteView.as_view(), name="advertisement-delete"),
    path('advertisements/<int:pk>/update/', AdvertisementUpdateView.as_view(), name="advertisement-update"),

]

app_name = "advertisement"
