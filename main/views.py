from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

import json

from .models import *
import random

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def majors(request):
    """
    Returns all the majors corresponding to a major id.
    """

    if request.method == 'GET':
        models = []
        for obj in Major.objects.all():
          models.append({
                "major_id": obj.id,
                "name": obj.name,
                "abbr": obj.abbr,
                "image_url": obj.image_url,
           })
        return HttpResponse(json.dumps(models))

@csrf_exempt
def classes(request):
    """
    Returns all the courses corresponding to a major_id.
    """
    if request.method == 'GET':
        mid = int(request.GET['major_id'])
        term = request.GET['term']

        try:
                m = Major.objects.get(id=mid)
        except:
                return HttpResponse(json.dumps([]))

        courses = Course.objects.filter(major=m)

        classes_sanitized = []

        for course in courses:
            classes = Class.objects.filter(term=term, course=course)

            for c in classes:
                class_obj = {}
                class_obj["class_id"]  = str(c.id)
                class_obj["class_name"] = str(c.course.name)
                class_obj["class_num"] = str(c.course.course_num)
                class_obj["professor_rating"] = int(c.professor.rating())

                #XXX: Calculate cost of each textbook correctly
                class_obj["osu_textbook_total"] = 100
                classes_sanitized.append(class_obj)

        return HttpResponse(json.dumps(classes_sanitized))


@csrf_exempt
def class_details(request):
    """
    Returns all the courses corresponding to a major_id.
    """
    if request.method == 'GET':
        class_id = request.GET.get('class_id', None)
        class_crn = request.GET.get('class_crn', None)

        if class_id:
            class_id = int(class_id)
            c = Class.objects.filter(id=class_id)[0]
        elif class_crn:
            c = Class.objects.filter(crn=class_crn)[0]
        else:
            return HttpResponse({"error": "error"})

        p = c.professor

        # Making days_of_week
        days_of_week = ""
        if c.mon:
            days_of_week += "M"
        if c.tue:
            days_of_week += "T"
        if c.wed:
            days_of_week += "W"
        if c.thu:
            days_of_week += "R"
        if c.fri:
            days_of_week += "F"

        cobj = {
            "class_id": str(c.id),
            "class_name": c.course.name,
            "class_num": c.course.course_num,
            "crn": c.crn,

        "major":{
                "name": c.course.major.name,
                "abbr": c.course.major.abbr, 
        },

        "professor": {
            "first_name": p.first_name,
            "last_name": p.last_name,
            "img_url": "",
            "rating": 5, 
        },

        "textbooks":[
                {
                   "name": "<string>",
                   "author": "<string>",
                   "isbn": "<string>",
                   "prices":[
                        {
                          "seller_name":"Amazon",
                          "price": "$13.40",
                          "link": "<url_string>",
                        }
                    ]
                },
            ],
        "days_of_week": days_of_week,  # (string to represent which days are present)
        "start_time": c.start_time,    # (24-hour two digit in PST),
        "end_time": c.end_time,
        "start_date": c.start_date, # (month/day/year),
        "end_date": c.end_date,
        }

        return HttpResponse(json.dumps(cobj, cls=DjangoJSONEncoder))


