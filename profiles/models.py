from django.conf import settings
from django.db import models

# Create your models here.
User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # deletes the user and all its data
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)


class Stocks(models.Model):
    symbol = models.OneToOneField(User, on_delete=models.CASCADE)
    nShares = models.IntegerField(null=True, blank=True)
    costPerShare = models.IntegerField(null=True, blank=True)
    totalGain = models.IntegerField(null=True, blank=True)
    totalGainInDollars = models.IntegerField(null=True, blank=True)


class WatchList(models.Model):
    symbolWatchlist = models.OneToOneField(User, on_delete=models.CASCADE)
