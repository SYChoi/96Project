from django.db import models
from account.models import Account

class Event(models.Model):
    eventID = models.IntegerField(primary_key=True)
    eventname = models.CharField(max_length=30)
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
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

