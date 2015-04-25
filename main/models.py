from django.db import models
from .helpers import *

class Course(models.Model):
    crn = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    course_num = models.CharField(max_length=4, null=True, blank=True) 
    # Just the num, not the course abbrv. E.g. CS101 would be stored as 101

    term = models.CharField(max_length=8, null=True, blank=True)

    # ForeginKey fields
    major = models.ForeignKey('Major', null=True, blank=True)
    professor = models.ForeignKey('Professor', null=True, blank=True)

    mon = models.BooleanField(default=False)
    tue = models.BooleanField(default=False)
    wed = models.BooleanField(default=False)
    thu = models.BooleanField(default=False)
    fri = models.BooleanField(default=False)

    # Start time and end time for class on any given day
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    # Start date and end date for the whole class
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    loc = models.CharField(max_length=32, null=True, blank=True)

    def __unicode__(self):
        return self.name + ': ' + self.term


class Professor(models.Model):
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)

    def rating(self):
       p = RateMyProf(self.first_name, self.last_name)
       p.get_data()
       return p.average_rating()


    def __unicode__(self):
        return self.name


class Textbook(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    course = models.ForeignKey('Course', null=True, blank=True)
    isbn = models.CharField(max_length=16, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)
    abbrv = models.CharField(max_length=8, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name
