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
                class_obj["professor_rating"] = int(c.professor.rating()[0])

                #XXX: Calculate cost of each textbook correctly
                books = Textbook.objects.filter(textbook_class = c)
                total = 0.0
                for book in books:
                        total += float(book.osu_price)
                class_obj["osu_textbook_total"] = "$"+str(total)
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

        ratings = p.rating()

        cobj = {
            "class_id": str(c.id),
            "class_name": c.course.name,
            "description": c.course.description,
            "class_num": c.course.course_num,
            "crn": c.crn,
            "lat": c.lat,
            "lon": c.lon,
        "major":{
                "name": c.course.major.name,
                "abbr": c.course.major.abbr, 
        },

        "professor": {
            "first_name": p.first_name,
            "last_name": p.last_name,
            "img_url": "",
            "rating": ratings[0], 
            "helpfulnes": ratings[1],
            "clarity": ratings[2],
           "easiness": ratings[3],
        },

        
        "days_of_week": days_of_week,  # (string to represent which days are present)
        "start_time": c.start_time,    # (24-hour two digit in PST),
        "end_time": c.end_time,
        "start_date": c.start_date, # (month/day/year),
        "end_date": c.end_date,
        }

        # Add textbooks
        books = Textbook.objects.filter(textbook_class = c)
        book_models = []
        for book in books:
                book_models.append({"name": book.name, 
                                    "author": "",
                                    "isbn": book.isbn,
                                    "prices": [{"seller_name": "OSU Book Store", "price":"$"+book.osu_price}, {"seller_name": "Amazon",
"price": "$"+book.amazon_price}]})

        cobj['textbooks'] = book_models
        return HttpResponse(json.dumps(cobj, cls=DjangoJSONEncoder))


@csrf_exempt
def search(request):
    """
    Returns all the classes and majors corresponding to a search term.
    """

    if request.method == 'GET':
        search_term = request.GET.get('q', None)

       # Get all majors
        major_name_pairs = Major.objects.all().values('id', 'name')
        matching_major_ids = []

        for pair in major_name_pairs:
            if pair['name'] and search_term.lower() in pair['name'].lower():
                matching_major_ids.append(pair['id'])

        major_models = []
        for obj in Major.objects.filter(id__in=matching_major_ids):
          major_models.append({
                "major_id": obj.id,
                "name": obj.name,
                "abbr": obj.abbr,
                "image_url": obj.image_url,
           })

       # Get all classes
        classes = Class.objects.filter(course__name__contains=search_term)
        class_models = []
        for c in classes:
            class_obj = {}
            class_obj["class_id"]  = str(c.id)
            class_obj["class_name"] = str(c.course.name)
            class_obj["class_num"] = str(c.course.course_num)
            class_obj["professor_rating"] = int(c.professor.rating())

            #XXX: Calculate cost of each textbook correctly
            class_obj["osu_textbook_total"] = 100
            class_models.append(class_obj)

        resp = {
                "classes":class_models,
                "majors":major_models,
        }

        return HttpResponse(json.dumps(resp, cls=DjangoJSONEncoder))
