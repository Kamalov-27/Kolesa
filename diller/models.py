from django.db import models

# Create your models here.
from auth_.models import User
from main.models import Car, City


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)



class Publications(Favourites):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    year = models.IntegerField()