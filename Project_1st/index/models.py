from django.db import models

class Event():
    eventname = models.CharField(min_length=1, max_length=30)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=50)
    detail = models.TextField()

    def register(self, form):
        eventname = form['eventname'].data
        date = form['date'].data
        time = form['time'].data
        place = form['place'].data
        detail = form['detail'].data

