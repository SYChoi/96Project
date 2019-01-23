from django.db import models
from django.contrib.auth.models import User

class Account(User):
    def register(self, form):
        username = form['username'].data
        password = form['password'].data
        try:
            new_user = Account.objects.create(username=username, password=password,)
            new_user.set_password(password)
            new_user.save()
        except:
            return False
        return True
