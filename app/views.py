from django.conf import settings
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

import paypal
from . import models

def home(request):

    context = {"contestants": models.Contestant.objects.all()}

    return render(request, "home.html", context=context)

class ContestantDetailView(DetailView):
    model = models.Contestant

# class HaircutDetailView(DetailView):
#     model = models.Haircut

class HaircutDetailView(DetailView):
    model = models.Haircut

def donateview(request,pk):
    try:
        c = models.Contestant.objects.get(pk=pk)
    except:
        raise Http404 
    ctx = {
        "paypal_url": settings.PAYPAL_URL,
        "paypal_id": settings.MERCHANT_ID,
        "paypal_return_url": request.build_absolute_uri(),
        "paypal_cancel_return_url": '',
        "contestant_name": ' '.join([c.first_name,c.last_name])
    }
    return render(request, "paypaltest.html", ctx)

# donation callback
def purchased(request,contestant):
    ctx = request.GET
    tx = request.GET['tx']
    result = paypal.Verify(tx)
    c = models.Contestant.objects.get(pk=contestant)
    if result.success() and ctx['amt'] == result.amount(): # valid
        donation = models.Donation.objects.create(transaction_id=tx,contestant=c,amount=float(result.amount()))
        return render(request, "purchasedone.html")
    # FIXME: display error message
    return HttpResponseForbidden()
