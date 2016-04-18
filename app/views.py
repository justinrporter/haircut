from decimal import Decimal

from django.shortcuts import render
from django.views.generic.detail import DetailView

from . import models

def home(request):

    context = {"contestants": models.Contestant.objects.all()}

    return render(request, "home.html", context=context)

class ContestantDetailView(DetailView):
    model = models.Contestant


# class HaircutDetailView(DetailView):
#     model = models.Haircut
