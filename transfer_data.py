import django
django.setup()

from main.models import *

import json
from dateutil.parser import parse

files = ['data/output', 'data/output2', 'data/output3']

for fname in files:
    f = open(fname)
    s = f.read()
    l = json.loads(s)

    for obj in l:
        major_abbr, course_num = obj['abbr'].split(' ')
        m, created = Major.objects.get_or_create(abbr=major_abbr)

        course, created = Course.objects.get_or_create(major=m, course_num=course_num, name=obj['title'],
                                                       credits=obj['credits'],
                                                       description=obj['desc'])

        classes = obj['classes']
        for c in classes:
            instructor_names = c['Instructor'].split(',')

            if len(instructor_names) == 2:
                first_name, last_name = instructor_names
            else:
                first_name = instructor_names[0]
                last_name = ""

            p, created = Professor.objects.get_or_create(first_name=first_name, last_name=last_name)

            try:
                c, created = Class.objects.get_or_create(crn=c['CRN'], professor=p, mon=c['M'], tue=c['T'], wed=c['W'], thu=c['R'], fri=c['F'], 
                      loc=c['Location'],  start_date=parse(c.get('startDate', '01/01/0000')).date(), end_date=parse(c.get('endDate', '01/01/0000')).date(),
                      start_time=parse(c.get('startTime', '00:00')).time(), end_time=parse(c.get('endTime', '00:00')).time(), term=c['Term'], course=course)
            except:
                print obj
