from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models import Sum


class Contestant(models.Model):
    #the user model should have email, name, etc.
    first_name = models.TextField(primary_key=True)
    last_name = models.TextField()

    bio = models.TextField()
    photo = models.ImageField()


class Donation(models.Model):

    contestant = models.ForeignKey(Contestant)
    amount = models.DecimalField(max_digits=6, decimal_places=2)


class Haircut(models.Model):

    name = models.TextField()
    description = models.TextField()

    contestant = models.ForeignKey(Contestant)
    photo = models.ImageField()

    goal_amount = models.DecimalField(max_digits=6, decimal_places=2)

    def progress(self):

        total_raised = Donation.objects.\
            filter(contestant=self.contestant).\
            aggregate(Sum('amount'))['amount__sum']

        progress = min(total_raised/self.goal_amount, 1) * 100

        return progress

