from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.home,
        name="home"),
    url(r'^paypaltest$',views.paypaltest,name="paypaltest"),
    url(r'^paypaltest/(?P<haircut>\w+)$',views.purchased,name="purchased")
]
