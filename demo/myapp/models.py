from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Crypto(models.Model):
    name = models.CharField(max_length=100)
    crypto_id = models.CharField(max_length=100)
    symbol = models.CharField(max_length=100)
    image_link = models.URLField(max_length=100)
    market_cap = models.DecimalField(null=True, blank=True, max_digits=100, decimal_places=2)
    circulating_supply = models.CharField(null=True, blank=True, max_length=100)