from django.test import TestCase

from comida.scraper import scrape_vendors_from_html

class ScraperTest(TestCase):

    def setUp(self):
        self.html_text = """<div class="otg-vendor-type otg-vendor-type-1"><div class="otg-vendor-type-name">Carts</div><table class="otg-vendors"><tbody><tr class="otg-vendor"><td class="otg-vendor-logo-container"><a class="otg-vendor-logo-link" href="http://www.aliciatamaleslosmayas.com" target="_blank"><img alt="Alicia&#039;s Tamales Los Mayas" class="otg-vendor-logo" src="http://media-cdn.offthegridmarkets.com/2013/04/516c7c1bea214_128x100.jpg" /></a></td><td class="otg-vendor-data"><div class="otg-vendor-name"><a class="otg-vendor-name-link" href="http://www.aliciatamaleslosmayas.com" target="_blank">Alicia&#039;s Tamales Los Mayas</a></div><div class="otg-vendor-cuisines"> Mexican	</div></td></tr></tbody></table></div></div>"""
       
    def test_scrape_vendors_from_html(self):
        self.assertEquals(len(scrape_vendors_from_html(self.html_text)), 1)    
