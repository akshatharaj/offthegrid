import datetime
import pytz

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from comida.models import Event, Vendor

class EventListView(ListView):

    model = Event
    queryset = Event.objects.filter(start_time__gt=datetime.datetime.now(tz=pytz.utc))
    paginate_by = 10


class EventDetailView(DetailView):

    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context['vendors'] = self.get_object().vendors.all()
        return context


class VendorListView(ListView):

    model = Vendor
    paginate_by = 10
    template_name = 'comida/vendor_list.html'
    # sorted results in really bad performance - http://stackoverflow.com/a/8478586/940859
    queryset = sorted(Vendor.objects.all(), key=lambda v: v.last_month_events, reverse=True)

    def get_context_data(self, **kwargs):
        context = super(VendorListView, self).get_context_data(**kwargs)
        return context


class VendorDetailView(DetailView):

    model = Vendor

    def get_context_data(self, **kwargs):
        context = super(VendorDetailView, self).get_context_data(**kwargs)
        now = datetime.datetime.now(tz=pytz.utc)
        thirty_days_back =  now - datetime.timedelta(days=30)
        context['events'] = self.get_object().event_set.filter(start_time__gte=thirty_days_back, start_time__lt=now)
        return context
