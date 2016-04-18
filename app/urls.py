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
        views.donateview,
        name='contestant-donate'),
    url(r'^contestant/(?P<pk>[-\w]+)/donate/callback?$',
        views.purchased,
        name='contestant-donate-callback'),
]