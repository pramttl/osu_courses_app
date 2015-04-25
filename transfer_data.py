import os
os.system("export DJANGO_SETTINGS_MODULE='osu_courses_app.settings'")

from main.models import *

import json
from dateutil.parser import parse

f = open('data/output')
s = f.read()
l = json.loads(s)

for ele in l:
    e = ele['classes']

    major_abbr, course_num = e['abbr'].split(' ')
    m, created = Major.objects.get_or_create(abbr=major_abbr)

    first_name, last_name = e['Instructor'].split(',')

    p, created = Professor.objects.get_or_create(first_name=first_name, last_name=last_name)

    c = Course(crn=e['CRN'], professor=p, mon=e['M'], tue=e['T'], wed=e['W'], thu=e['R'], fri=e['F'], 
          loc=e['Location'],  start_date=parse(e['startDate']).date(), end_date=parse(e['endDate']).date(),
          start_time=parse(e['startTime']).time(), end_time=parse(e['endTime']).time(), major=m,
          term=e['Term'], course_num=course_num, name=e['Title'])

    c.save()
