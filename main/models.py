from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User




class Car(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)


class City(models.Model):
    name = models.CharField(max_length=150)

