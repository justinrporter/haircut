from __future__ import unicode_literals

from django.db import models
from django.conf import settings

class Contestant(models.Model):
    #the user model should have email, name, etc.
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    bio = models.TextField()
    pic = models.ImageField()

    # maybe not necessary, but you'll be able to call contestant.first_name
    # intstead of contestant.user.first_name
    def first_name(self):
        return user.first_name
    def last_name(self):
        return user.last_name

class Haircut(models.Model):

    name = models.TextField()
    description = models.TextField()

    contestant = models.ForeignKey(Contestant)
    photo = models.ImageField()

    goal_amount = models.DecimalField(max_digits=6, decimal_places=2)

class Donation(models.Model):

    contestant = models.ForeignKey(Contestant)
    goal_amount = models.DecimalField(max_digits=6, decimal_places=2)
