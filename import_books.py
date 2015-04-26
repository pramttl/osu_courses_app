import django
import urllib2
import json
import time

django.setup()

from main.models import *

#Example URL:
#http://verbacompare.osubeaverstore.com/compare/books?id=2015-Winter__AG__412__400

termMapping = {'F15': '2015-Fall', 'W15': '2015-Winter', 'W16': '2016-Winter', 'Sp15': '2015-Spring', 'Su15': '2015-Summer'}

for c in Class.objects.all():
        s = 'http://verbacompare.osubeaverstore.com/compare/books?id=%s__%s__%s__001' % (termMapping[c.term], c.course.major.abbr,
c.course.course_num)

        try:
                stream = urllib2.urlopen(s)
        except:
                continue
        
        books = json.loads(stream.read())

        for book in books:
                book, created = Textbook.objects.get_or_create(name=book['title'], isbn=book['isbn'], osu_price=book['offers'][0]['price'],
textbook_class=c)
        
