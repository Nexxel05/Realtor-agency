from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from advertisement.forms import RealtorCreationForm, AdvertisementCreationForm, RealtorUpdateForm, RealtorSearchForm
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

    def get_queryset(self):
        queryset = super().get_queryset()
        form = RealtorSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                Q(first_name__icontains=form.cleaned_data["search"]) |
                Q(last_name__icontains=form.cleaned_data["search"]) |
                Q(username__icontains=form.cleaned_data["search"])
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search = self.request.GET.get("search", "")

        context["search_form"] = RealtorSearchForm(initial={
            "search": search
        })
        return context


class RealtorDetailView(LoginRequiredMixin, DetailView):
    model = Realtor


class RealtorCreateView(LoginRequiredMixin, CreateView):
    model = Realtor
    form_class = RealtorCreationForm


class RealtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Realtor
    form_class = RealtorUpdateForm


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


class PropertyDeleteView(LoginRequiredMixin, DeleteView):
    model = Property
    success_url = reverse_lazy("advertisement:property-list")


class PropertyUpdateView(LoginRequiredMixin, UpdateView):
    model = Property
    fields = ("name", )


class AdvertisementListView(LoginRequiredMixin, ListView):
    model = Advertisement


class AdvertisementDetailView(LoginRequiredMixin, DetailView):
    model = Advertisement


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = AdvertisementCreationForm


class AdvertisementDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertisement
    success_url = reverse_lazy("advertisement:advertisement-list")


class AdvertisementUpdateView(LoginRequiredMixin, UpdateView):
    model = Advertisement
    form_class = AdvertisementCreationForm
