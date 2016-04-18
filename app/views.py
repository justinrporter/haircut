from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseForbidden
import models
import paypal

def home(request):
    return render(request, "home.html")

def paypaltest(request):
    ctx = {
        "paypal_url": settings.PAYPAL_URL,
        "paypal_id": settings.MERCHANT_ID,
        "paypal_return_url": "http://127.0.0.1:8000/app/paypaltest/"+"foo",
        "paypal_cancel_return_url": "http://127.0.0.1:8000"
    }
    return render(request, "paypaltest.html", ctx)

# donation callback
def purchased(request,contestant):
    ctx = request.GET
    tx = request.GET['tx']
    result = paypal.Verify(tx)
    if result.success() and ctx['amt'] == result.amount(): # valid
        donation = models.Donation(transaction_id=tx,contestant=contestant,goal_amount=result.amount())
        donation.save()
        return render(request, "purchasedone.html")
    # FIXME: display error message
    return HttpResponseForbidden()