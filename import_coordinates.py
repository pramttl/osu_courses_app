import django
django.setup()

from main.models import *

for line in open('data/osu_building_coordinates.txt'):
        line = line.replace('\n', '')
        elems = line.split(',')

        print elems
        
        try:
            if len(elems) == 4:
                ed = elems[0].lower()
                Class.objects.filter(loc__icontains=ed).update(lat=elems[2], lon=elems[3])
        except:
            pass
