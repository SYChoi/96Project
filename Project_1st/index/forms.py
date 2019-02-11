from django import forms

class EventregForm(forms.Form):
    eventname = forms.CharField(max_length=30)
    date = forms.DateField()
    time = forms.TimeField()
    place = forms.CharField(max_length=50)
    detail = forms.TextField()
