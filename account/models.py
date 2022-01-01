from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=14, default='')
    favt_food = models.CharField(max_length=100)
    favt_place = models.CharField(max_length=100)
    balance=models.FloatField(default=0.0)

    def getname(self):
        return self.name
