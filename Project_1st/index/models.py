from django.db import models
from account.models import Account

class Event(models.Model):
    eventname = models.CharField(db_index=True, max_length=30, primary_key=True)
    user = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    place = models.CharField(max_length=50)
    detail = models.TextField()

    def register(self, form, request):
        eventname = form['eventname'].data
        date = form['date'].data
        time = form['time'].data
        place = form['place'].data
        detail = form['detail'].data
        try:
            new_event = Event.objects.create(
                eventname = eventname,
                user = request.user, 
                date = date,
                time = time,
                place = place,
                detail = detail,
            )
        except:
            return False
        return True

