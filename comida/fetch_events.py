import datetime
import pytz

from nltk.tokenize import RegexpTokenizer  
from django.conf import settings 
from facepy import GraphAPI, utils
from comida.models import Event, Vendor

def get_vendors_from_description(desc):
    # we care only about word characters
    tokenizer = RegexpTokenizer(r'\w+')  
    event_vendors = []
    try: 
	    desc_tokens = set(tokenizer.tokenize(desc))
	    for vendor in Vendor.objects.all():
	    	# tokenizing vendor name from database(html)
	    	vendor_name_tokens = set(tokenizer.tokenize(vendor.name))
	    	# if next line is a false, we are 100% sure that vendor is not in description!
	    	if len(desc_tokens.intersection(vendor_name_tokens)) == len(vendor_name_tokens):
	    		# For incresed accuracy, double check if vendor name is 
	    		# a substring of description
	    		if vendor.name in desc: 
	    			event_vendors.append(vendor)
    except TypeError: 
        # got trash description from facebook, do nothing
	pass
    return event_vendors


def add_vendors_to_event(event, vendors):
    current_vendors = event.vendors.all()
    # adding list of vendors on this event database object, if they dont already exist
    for vendor in vendors:
        if vendor not in current_vendors:
            event.vendors.add(vendor)
	

def get_api_connection():
    access_token = utils.get_application_access_token(settings.FACEBOOK_APP_ID, 
                          settings.FACEBOOK_APP_SECRET)
    # Create GraphAPI instance to interact with Facebook API
    return GraphAPI(access_token) 


def get_events_from_facebook():
    fb_api = get_api_connection()
    first_page = 'OffTheGridSF/events'
    next = first_page
    while(True):
        events = fb_api.get(next)
        # iterate over all events in response
        for event in events.get('data'):
            event_fb_id = event.get('id')
            # go fetch full description
            full_event_info = fb_api.get(event_fb_id)
            try:
                # if event exists in the database, Update it with most recent info 
                event_from_db = Event.objects.get(fb_id=event_fb_id)
                # is it an on-going or up-coming event? If not, we dont care
                if event_from_db.end_time and (event_from_db.end_time >= datetime.datetime.now(tz=pytz.utc)):
                	# event description might have changed (new vendors added). Figure out vendors again 
                	participating_vendors = get_vendors_from_description(full_event_info.get('description'))
                	add_vendors_to_event(event_from_db, participating_vendors)

	                for key in full_event_info:
	                	if hasattr(event_from_db, key) and not key == 'id':
	                		setattr(event_from_db, key, full_event_info.get(key))

	                event_from_db.save()
            except Event.DoesNotExist:
            	# new event, figure out participating vendors
                participating_vendors = get_vendors_from_description(full_event_info.get('description'))
                del full_event_info['owner']
                full_event_info['fb_id'] = full_event_info.pop('id') 
                new_event = Event.objects.get_or_create(**full_event_info)[0]
                add_vendors_to_event(new_event, participating_vendors)

        if events.get('paging').get('next', None) is None:
            break
        else:
            next = first_page + '?after=%s' % events.get('paging').get('cursors').get('after')



