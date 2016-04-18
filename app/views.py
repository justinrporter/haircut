from django.conf import settings
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, redirect
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

def donation_view(request,pk):
    try:
        c = models.Contestant.objects.get(pk=pk)
    except:
        raise Http404 
    return_url = request.build_absolute_uri()
    if not return_url.endswith('/'):
        return_url += '/'
    return_url += 'callback'
    ctx = {
        "paypal_url": settings.PAYPAL_URL,
        "paypal_id": settings.MERCHANT_ID,
        "paypal_return_url": return_url,
        "paypal_cancel_url": request.build_absolute_uri('/'),
        "contestant_name": ' '.join([c.first_name,c.last_name])
    }
    return render(request, "donation_view.html", ctx)

# donation callback
def donation_callback_view(request,pk):
    ctx = request.GET
    tx = request.GET['tx']
    result = paypal.Verify(tx)
    c = models.Contestant.objects.get(pk=pk)
    if result.success() and ctx['amt'] == result.amount(): # valid
        donation = models.Donation.objects.create(transaction_id=tx,contestant=c,amount=float(result.amount()),email=result.email())
        return redirect('contestant-detail',pk=pk)
    # FIXME: display error message
    return HttpResponseForbidden()
