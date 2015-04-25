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

