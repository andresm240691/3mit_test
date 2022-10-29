from django.db import models

# Create your models here.


class CoinModel(models.Model):
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
