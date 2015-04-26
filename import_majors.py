import django
django.setup()

from main.models import *

for line in open('data/majors.txt'):
        line = line.replace('\n', '')
        elems = line.split(',')
        
        if len(elems) == 2:
                try:
                        maj = Major.objects.filter(abbr=elems[0])[0]
                        maj.name = elems[1]
                        maj.save()
                except:
                        pass

