import re
from lxml import html
import requests
from comida.models import Vendor

def get_vendor_html():
    #fetch html from offthegridsf website
    WEB_URL = 'http://offthegridsf.com/vendors'
    page = requests.get(WEB_URL)
    return page.text

def scrape_vendors_from_html(html_content):
    """
    parse html get all vendors' information
    """
    # if source html changes, all this code wont work as expected
    vendors_list = []
    tree = html.fromstring(html_content)
    vendor_types = [k.text for k in tree.xpath('//div[@class="otg-vendor-type-name"]')]
    for table in tree.xpath('//table'):
        vendor_type = vendor_types.pop(0)
        for row in table.xpath('.//tr'):
            vendor = {'logo': row.xpath('.//td')[0].find('.//img').get('src'),
                       'name': row.xpath('.//td')[1].find('.//a').text,
                       'website': row.xpath('.//td')[1].find('.//a').get('href'),
                       'cuisine': re.sub("[^\w', ]", '', row.xpath('.//div[@class="otg-vendor-cuisines"]')[0].text),
                       'vendor_type': vendor_type}
            vendors_list.append(vendor)
    return vendors_list      

def get_or_create_vendors(vendors):
    for vendor in vendors:
        Vendor.objects.get_or_create(**vendor)

if __name__=='__main__':
    get_or_create_vendors(scrape_vendors_from_html(get_vendor_html()))
