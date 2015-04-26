import django
import urllib2
import json
import time

django.setup()

from main.models import *
from amazon.api import AmazonAPI

#Access Key, Secret Key, Assoc Tag
amazon = AmazonAPI('AKIAJWBKRIZ6TNTNDR7A', 'HU67Mum3v7obUhfl7bdB24uxV497eqj7L4g4vQaW', 'hac078-20')

for book in Textbook.objects.all():
        #Input any keywords here
        keywordInput = book.isbn
        try:
                products = amazon.search_n(1, Keywords=keywordInput, SearchIndex='All')
                if len(products) > 0:
                        book.amazon_price = products[0].price_and_currency[0]
                        print "Found Book: ", book.id, book.amazon_price
                        book.cover_url = products[0].large_image_url
                        book.save()
        except:
                pass
