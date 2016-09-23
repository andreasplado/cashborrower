from django.db import models

# Create your models here.
class Event(models.Model):
    eventName = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    def __str__(self):
        return self.eventName

