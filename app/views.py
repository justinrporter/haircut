from django.shortcuts import render
from django.views.generic.detail import DetailView

from . import models

def home(request):
    return render(request, "home.html")

class ContestantDetailView(DetailView):
    model = models.Contestant

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        # TODO: add in $$

        return context

class HaircutDetailView(DetailView):
    model = models.Haircut
