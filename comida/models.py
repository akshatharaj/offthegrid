import datetime
import pytz
from django.db import models

class Event(models.Model):
    description = models.TextField()
    name = models.CharField(max_length="100")
    location = models.CharField(max_length="200")
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    timezone = models.CharField(max_length="100", null=True, blank=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    privacy = models.CharField(max_length="100")
    is_date_only = models.BooleanField(null=False)
    fb_id = models.CharField(max_length="100", null=False, blank=False, db_index=True)
    vendors = models.ManyToManyField('Vendor')

    class Meta:
        get_latest_by = 'start_time'

    def __unicode__(self):
        return self.name



class Vendor(models.Model):
    name = models.CharField(max_length="100")
    description = models.TextField()
    cuisine = models.CharField(max_length="200")
    vendor_type = models.CharField(max_length=25, null=False, blank=False, default='Trucks')
    logo = models.CharField(max_length=1000, null=True, blank=True)
    website = models.CharField(max_length=500, null=True, blank=True)

    def __unicode__(self):
    	return self.name

    def serves_cuisine(self, cuisine):
        return cuisine.lower() in self.cuisine.lower()

    @property
    def last_month_events(self): 
        now = datetime.datetime.now(tz=pytz.utc)
        thirty_days_back =  now - datetime.timedelta(days=30)
        return self.event_set.filter(start_time__gte=thirty_days_back, start_time__lt=now).count()

