from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

import json

from .models import *
import random

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    """
    Test url
    """
    return HttpResponse(json.dumps({ "test" : "success"}))


@csrf_exempt
def majors(request):
    """
    Returns all the majors corresponding to a major id.
    """
    if request.GET:
        return HttpResponse(json.dumps(Major.objects.all()))


@csrf_exempt
def courses(request):
    """
    Returns all the courses corresponding to a major_id.
    """
    if request.GET:
        mid = request.GET['major_id']
        term = request.GET['term']

        m = Major.objects.get(id=mid)
        courses = Course.objects.filter(major=m.id)

        courses_sanitized = []

        cobj = {}
        for c in courses:
            cobj["course_id"]  = str(c.id),
            cobj["course_name"] = str(c.name),
            cobj["course_num"] = str(c.course_num),
            cobj["professor_rating"] = int(c.professor.rating),

            #XXX: Calculate cost of each textbook correctly
            cobj["osu_textbook_total"] = 10
            courses_sanitized.append(cobj)

        return HttpResponse(json.dumps(courses_sanitized))


@csrf_exempt
def course_details(request):
    """
    Returns all the courses corresponding to a major_id.
    """
    if request.GET:
        cid = request.GET['course_id']

        c = Course.objects.get(id=cid)
        p = c.professor

        # Making days_of_week
        days_of_week = ""
        if course.mon:
            days_of_week += "M"
        if course.tue:
            days_of_week += "T"
        if course.wed:
            days_of_week += "W"
        if course.thu:
            days_of_week += "R"
        if course.fri:
            days_of_week += "F"

        cobj = {
            "course_id": "<string>",
            "course_name": "Multimedia Systems",
            "course_num": "477",
            "crn":"<string>",

        "major":{
                "name": "Electrical and Computer Engineering",
                "abbrv": "ECE", 
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
            "start_date": c.start_date # (month/day/year),
            "end_date": c.end_date,
        }


