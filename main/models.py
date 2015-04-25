from django.db import models


class Course(models.Model):
    """
    Contains the JSON question
    """
    crn = models.CharField(max_length=16, null=True, blank=True)
    name = models.CharField(max_length=32, null=True, blank=True)
    term = models.CharField(max_length=8, null=True, blank=True)
    professor = models.ForeignKey('Professor')

    def __unicode__(self):
        return self.name + ': ' + self.term


class Professor(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Textbook(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    course = models.ForeignKey('Course')
    isbn = models.CharField(max_length=16, null=True, blank=True)

    def __unicode__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=16, null=True, blank=True)

    def __unicode__(self):
        return self.name
