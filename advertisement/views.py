from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView
)

from advertisement.forms import (
    RealtorCreationForm,
    AdvertisementCreationForm,
    RealtorUpdateForm,
    RealtorSearchForm,
    AdvertisementSearchForm
)
from advertisement.models import Realtor, Advertisement, PropertyType, City


@login_required
def index(request):
    num_of_realtors = Realtor.objects.count() - 1
    num_of_advertisements = Advertisement.objects.count()
    num_of_cities = City.objects.count()

    context = {
        "num_of_realtors": num_of_realtors,
        "num_of_advertisements": num_of_advertisements,
        "num_of_cities": num_of_cities,
    }
    return render(request, "advertisement/index.html", context)


class RealtorListView(LoginRequiredMixin, ListView):
    model = Realtor
    paginate_by = 3

    def get_queryset(self):
        queryset = Realtor.objects.exclude(username="admin")
        form = RealtorSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                Q(first_name__icontains=form.cleaned_data["search"]) | Q(
                    last_name__icontains=form.cleaned_data["search"]) | Q(
                    username__icontains=form.cleaned_data["search"]
                )
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super(RealtorListView, self).get_context_data()

        search = self.request.GET.get("search", "")

        context["search_form"] = RealtorSearchForm(initial={
            "search": search
        })

        return context


class RealtorDetailView(LoginRequiredMixin, DetailView):
    model = Realtor

    def get_object(self, queryset=None):
        return get_object_or_404(Realtor, id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        context["num_of_successful_deals"] = \
            self.get_object().advertisements.filter(sold=True).count()

        return context


class RealtorCreateView(LoginRequiredMixin, CreateView):
    model = Realtor
    form_class = RealtorCreationForm


class RealtorUpdateView(LoginRequiredMixin, UpdateView):
    model = Realtor
    form_class = RealtorUpdateForm


class RealtorDeleteView(LoginRequiredMixin, DeleteView):
    model = Realtor
    success_url = reverse_lazy("advertisement:realtor-list")


class PropertyTypeListView(LoginRequiredMixin, ListView):
    model = PropertyType
    paginate_by = 10


class AdvertisementListView(LoginRequiredMixin, ListView):
    model = Advertisement
    paginate_by = 5

    def get_queryset(self):
        queryset = Advertisement.objects.all().select_related("city")

        cities = self.request.GET.getlist("cities")

        if cities:
            return self.model.objects.filter(
                city__in=cities
            ).distinct()

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdvertisementListView, self).get_context_data()

        context["search_form"] = AdvertisementSearchForm()

        return context


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


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("advertisement:advertisement-create")


@login_required
def change_advertisement_status(request, pk):
    advertisement = get_object_or_404(Advertisement, id=pk)

    advertisement.sold = not advertisement.sold

    advertisement.save()

    return render(
        request,
        "advertisement/advertisement_detail.html",
        context={"advertisement": advertisement}
    )
