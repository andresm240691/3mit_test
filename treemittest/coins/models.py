from django.db import models
from django.contrib.auth.models import User


class Coin(models.Model):
    table_index = models.IntegerField(null=True)
    img_src = models.CharField(null=True, blank=True, max_length=250)
    name = models.CharField(max_length=150)
    symbol = models.CharField(max_length=100, unique=True)
    price = models.FloatField(null=True)
    percentage_one_hour = models.CharField(
        max_length=50, null=True, blank=True)
    percentage_twentyfour_hour = models.CharField(
        max_length=50, null=True, blank=True)
    percentage_seven_days = models.CharField(
        max_length=50, null=True, blank=True)
    percentage_thirtyeight_days = models.CharField(
        max_length=50, null=True, blank=True)
    volume = models.FloatField(null=True)
    circulating_quantity = models.FloatField(null=True)
    total_quantity = models.CharField(
        max_length=50, null=True, blank=True)


class BriefCase(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_quantity = models.FloatField(null=True)
    average_purchase = models.FloatField(null=True)
    TREN_CHOICES = [
        ('POSITIVE', 'POSITIVE'),
        ('NEGATIVE', 'NEGATIVE'),
    ]
    trend = models.CharField(
        max_length=10,
        choices=TREN_CHOICES,
        default='POSITIVE',
    )


class Operation(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_quantity = models.FloatField(null=True)
    amount = models.FloatField(null=True)
    briefcase = models.ForeignKey(BriefCase, on_delete=models.CASCADE)