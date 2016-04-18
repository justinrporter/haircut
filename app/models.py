from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Contestant(models.Model):
    #the user model should have email, name, etc.
    first_name = models.TextField(primary_key=True)
    last_name = models.TextField()

    bio = models.TextField()
    pic = models.ImageField()

class Haircut(models.Model):

    name = models.TextField()
    description = models.TextField()

    contestant = models.ForeignKey(Contestant)
    photo = models.ImageField()

    goal_amount = models.DecimalField(max_digits=6, decimal_places=2)

class Donation(models.Model):

    transaction_id = models.CharField(max_length=250)
    contestant = models.ForeignKey(Contestant)
    goal_amount = models.DecimalField(max_digits=6, decimal_places=2)
    email = models.TextField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)