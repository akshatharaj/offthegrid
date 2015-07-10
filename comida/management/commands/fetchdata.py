from django.core.management.base import BaseCommand, CommandError
from comida import scraper
from comida.fetch_events import get_events_from_facebook

class Command(BaseCommand):
    help = 'Loads vendors and events information into database'

    def handle(self, *args, **options):
        scraper.get_or_create_vendors(scraper.scrape_vendors_from_html(scraper.get_vendor_html()))
        get_events_from_facebook()
        self.stdout.write('Successfully loaded vendors and events into database')




