from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()



class Car(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class City(models.Model):
    name = models.CharField(max_length=150)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)



class Publications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    year = models.IntegerField()
