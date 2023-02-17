from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from advertisement.forms import RealtorCreationForm, AdvertisementCreationForm, RealtorUpdateForm
from advertisement.models import Realtor, Advertisement, Property


def index(request):
    num_of_realtors = Realtor.objects.count()
    num_of_advertisements = Advertisement.objects.count()

    context = {
        "num_of_realtors": num_of_realtors,
        "num_of_advertisements": num_of_advertisements
    }
    return render(request, "advertisement/index.html", context)


class RealtorListView(ListView):
    model = Realtor


class RealtorDetailView(DetailView):
    model = Realtor


class RealtorCreateView(CreateView):
    model = Realtor
    form_class = RealtorCreationForm
    success_url = reverse_lazy("advertisement:realtor-list")


class RealtorUpdateView(UpdateView):
    model = Realtor
    form_class = RealtorUpdateForm
    success_url = reverse_lazy("advertisement:realtor-list")


class RealtorDeleteView(DeleteView):
    model = Realtor
    success_url = reverse_lazy("advertisement:realtor-list")


class PropertyListView(ListView):
    model = Property


class PropertyDetailView(DetailView):
    model = Property


class PropertyCreateView(CreateView):
    model = Property
    fields = ("name",)
    success_url = reverse_lazy("advertisement:property-list")


class PropertyDeleteView(DeleteView):
    model = Property
    success_url = reverse_lazy("advertisement:property-list")


class AdvertisementListView(ListView):
    model = Advertisement


class AdvertisementDetailView(DetailView):
    model = Advertisement


class AdvertisementCreateView(CreateView):
    model = Advertisement
    form_class = AdvertisementCreationForm
    success_url = reverse_lazy("advertisement:advertisement-list")


class AdvertisementDeleteView(DeleteView):
    model = Advertisement
    success_url = reverse_lazy("advertisement:advertisement-list")


class AdvertisementUpdateView(UpdateView):
    model = Advertisement
    form_class = AdvertisementCreationForm
    success_url = reverse_lazy("advertisement:advertisement-list")