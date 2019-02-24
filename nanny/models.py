from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class myUser(User):
    phone = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    class Meta:
        abstract = True

class Host(myUser):
    kids = models.IntegerField(default=1)


class Nanny(myUser):
    price = models.IntegerField(default=1)

class Schedule(models.Model):
    host = models.ForeignKey(Host,on_delete = models.CASCADE)
    nanny = models.ForeignKey(Nanny,on_delete = models.CASCADE)
    time = models.CharField(max_length=200)
    payment = models.IntegerField(default=0)

class Note(models.Model):
    host = models.ForeignKey(Host,on_delete=models.CASCADE)
    nanny = models.ForeignKey(Nanny,on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
