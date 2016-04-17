from django.shortcuts import render

# PAYMENT_TRANSFER_TOKEN = "k1OPFc7pSY2TkX1sX4-EecbL8vyWWlSkH8dg03u5xBXrF6lW8ehQGpvkWY8"
PAYMENT_TRANSFER_TOKEN = "PRr9RXwqJn1k2HTnFNk5J19vKntMe8SfmIne90DIfURqRYGce_ZD-QgQBMe"
PAYPAL_URL = 'https://www.sandbox.paypal.com/au/cgi-bin/webscr'


# MERCHANT_ID = "WVUT663HTXM3Q"
MERCHANT_ID = "L8KF3JYDVNWTS"

# live
#PAYPAL_URL = 'https://www.paypal.com/au/cgi-bin/webscr'
#PAYPAL_PDT_URL = 'https://www.paypal.com/au/cgi-bin/webscr'

def home(request):
    return render(request, "home.html")

def paypaltest(request):
    ctx = {
        "paypal_url": PAYPAL_URL,
        "paypal_id": MERCHANT_ID,
        "paypal_return_url": "http://127.0.0.1:8000/paypaltest/"+"foo"+"done",
        "paypal_cancel_return_url": "http:127.0.0.1:8000"
    }
    return render(request, "paypaltest.html", ctx)

# donation callback
def purchased(request,haircut):
    ctx = request
    return render(request, "purchasedone.html", ctx)