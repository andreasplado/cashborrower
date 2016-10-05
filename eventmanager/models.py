from __future__ import unicode_literals

from django.db import models
from datetime import datetime


# Create your models here.

class Event(models.Model):
    eventName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.eventName

class Comment(models.Model):
    event = models.ForeignKey(Event)
    comment = models.CharField(max_length=100)
    def __str__(self):
        return self.comment

class EventLike(models.Model):
    event = models.ForeignKey(Event)

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)


