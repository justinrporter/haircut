from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.home,
        name="home"),
    url(r'^contestant/(?P<pk>[-\w]+)/?$',
        views.ContestantDetailView.as_view(),
        name='contestant-detail'),
    url(r'^contestant/(?P<pk>[-\w]+)/donate/?$',
        views.donation_view,
        name='contestant-donate'),
    url(r'^contestant/(?P<pk>[-\w]+)/donate/callback?$',
        views.donation_callback_view,
        name='contestant-donate-callback'),
]