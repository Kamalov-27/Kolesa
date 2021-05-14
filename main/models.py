from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Car(City):
    description = models.TextField(blank=True)


class Category(City):
    description = models.TextField(blank=True)



