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

    def __str__(self):
        return self.name

