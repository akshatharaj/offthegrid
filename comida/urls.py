from django.conf.urls import url
from comida.views import EventListView, EventDetailView, VendorListView, VendorDetailView

urlpatterns = [
    url(r'^events/$', EventListView.as_view(), name='event-list'),
    url(r'^events/(?P<pk>\d+)/$', EventDetailView.as_view(), name='event-detail'),

    url(r'^vendors/$', VendorListView.as_view(), name='vendor-list'),
    url(r'^vendors/(?P<pk>\d+)/$', VendorDetailView.as_view(), name='vendor-detail'),
]