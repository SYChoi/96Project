from django.db import models

class Post(models.Model):
	name = models.CharField(max_length = 100, blank = False)
	date = models.DateField(auto_now_add=True)
	content = models.CharField(max_length = 10000, blank = True)
