from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.CharField(max_length=2)
    date = models.CharField(max_length=50)
    creditcard = models.CharField(max_length=50)
    