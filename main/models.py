from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class AbstractModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True


class CityManager(models.Manager):

    def order_by_name(self):
        return self.filter().order_by('name')

class City(AbstractModel):


    objects = CityManager()

    def __str__(self):
        return self.name

class CarManager(models.Manager):

    def order_by_name(self):
        return self.filter().order_by('name')

class Car(AbstractModel):


    objects = CarManager()
    def __str__(self):
        return self.name

class Category(AbstractModel):

<<<<<<< HEAD
class SubCategory(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
=======
    def __str__(self):
        return self.name
>>>>>>> c0c99cb96e54c2efe888f20922620d98b643636a

    def __str__(self):
        return self.name

# 
# class EngineType(models.Model):
#     name
