from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Crypto(models.Model):
    name = models.CharField(max_length=100)
    market_cap = models.IntegerField(default=False)