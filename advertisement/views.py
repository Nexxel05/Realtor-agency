from django.shortcuts import render
from django.views.generic import ListView, DetailView

from advertisement.models import Realtor, Advertisement


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

