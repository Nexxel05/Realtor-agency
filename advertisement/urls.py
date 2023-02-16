from django.urls import path

from advertisement.views import (
    index,
    RealtorListView,
    RealtorDetailView,
    PropertyListView,
    PropertyDetailView
)

urlpatterns = [
    path('', index, name="index"),
    path('realtors/', RealtorListView.as_view(), name="realtor-list"),
    path('realtors/<int:pk>', RealtorDetailView.as_view(), name="realtor-detail"),
    path('properties/', PropertyListView.as_view(), name="property-list"),
    path('properties/<int:pk>', PropertyDetailView.as_view(), name="property-detail"),

]

app_name = "advertisement"
