from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from advertisement.forms import RealtorCreationForm, AdvertisementCreationForm, RealtorUpdateForm
from advertisement.models import Realtor, Advertisement, Property


@login_required
def index(request):
    num_of_realtors = Realtor.objects.count()
    num_of_advertisements = Advertisement.objects.count()

    context = {
        "num_of_realtors": num_of_realtors,
        "num_of_advertisements": num_of_advertisements
    }
    return render(request, "advertisement/index.html", context)


class RealtorListView(LoginRequiredMixin, ListView):
    model = Realtor


class RealtorDetailView(LoginRequiredMixin, DetailView):
    model = Realtor


class RealtorCreateView(LoginRequiredMixin, CreateView):
    model = Realtor
    form_class = RealtorCreationForm
    success_url = reverse_lazy("advertisement:realtor-list")


class RealtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Realtor
    form_class = RealtorUpdateForm
    success_url = reverse_lazy("advertisement:realtor-list")


class RealtorDeleteView(LoginRequiredMixin, DeleteView):
    model = Realtor
    success_url = reverse_lazy("advertisement:realtor-list")


class PropertyListView(LoginRequiredMixin, ListView):
    model = Property


class PropertyDetailView(LoginRequiredMixin, DetailView):
    model = Property


class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    fields = ("name",)
    success_url = reverse_lazy("advertisement:property-list")


class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    success_url = reverse_lazy("advertisement:property-list")


class AdvertisementListView(LoginRequiredMixin, ListView):
    model = Advertisement


class AdvertisementDetailView(LoginRequiredMixin, DetailView):
    model = Advertisement


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementCreationForm
    success_url = reverse_lazy("advertisement:advertisement-list")


class AdvertisementDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertisement
    success_url = reverse_lazy("advertisement:advertisement-list")


class AdvertisementUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementCreationForm
    success_url = reverse_lazy("advertisement:advertisement-list")