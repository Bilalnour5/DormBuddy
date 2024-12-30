from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class shop(models.Model):
    house = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(AbstractUser):
    email = models.EmailField(unique=True)