from django.urls import path

from advertisement.views import index, RealtorListView

urlpatterns = [
    path('', index, name="index"),
    path('realtors/', RealtorListView.as_view(), name="realtor-list"),
]

app_name = "advertisement"
