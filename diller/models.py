from django.db import models

# Create your models here.
from auth_.models import User
from main.models import Car, City

class FavoritesManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    objects = FavoritesManager

class Publications(models.Manager):
    def order_by_year(self):
        return self.filter().order_by('year')

class Publications(Favourites):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()
    year = models.IntegerField()

class ArchiveManager(models.Manager):
    def for_car(self, car):
        return self.filter(car=car)

class Archive(Favourites):

    objects = ArchiveManager