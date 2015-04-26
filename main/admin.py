from django.contrib import admin

from .models import *

admin.site.register(Major)
admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Professor)
admin.site.register(Textbook)