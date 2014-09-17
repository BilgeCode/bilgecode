from django.db import models
from django.contrib.auth.models import User


CONTRIBUTION_TYPES = (
    ('one-time', "One Time"),
    ('backer', "Backer"),
    ('pledge', "Plege")
)


class Contributions(models.Model):
    """
        Stores all cleared contributions

        Contributions can come in three ways
    """
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKeyField(User)
    amount = models.FloatField()
    stripe_token = models.CharField(max_length=32)
    type = models.ChoiceField(choices=CONTRIBUTION_TYPES)
    pledge = models.ForeignKeyField('Pledge', blank=True, null=True)
    level = models.ForeignKeyField('BackerLevel', blank=True, null=True)


class BackerLevel(models.Model):
    """
        Subscription Levels
    """
    name = models.CharField(max_length=32)
    amount = models.FloatField()


class Feature(models.Model):
    """
        Features that have been requested/proposed
    """
    name = models.CharField(max_length=128)
    description = models.TextField()
    complete = models.BooleanField(default=False)


class Pledge(models.Model):
    """
        Pledges of contributions towards features
    """
    feature = models.ForeignKey(Feature)
    amount = models.FloatField()
    date_pledged = models.DateField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    date_paid = models.DateField(blank=True, null=True)
