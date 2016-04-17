from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^contestant/(?P<pk>[-\w]+)/$',
        views.ContestantDetailView.as_view(),
        name='contestant-detail'),
    url(r'^haircut/(?P<pk>[-\w]+)/$',
        views.HaircutDetailView.as_view(),
        name='haircut-detail'),
]