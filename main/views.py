from django.shortcuts import render_to_response
from django.http import HttpResponse
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
    return HttpResponse("None")