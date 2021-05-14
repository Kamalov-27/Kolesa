from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from diller.models import Favourites
from . import models

@receiver(post_save, sender=models.User)
def developer_created(sender, instance, created, **kwargs):
    if created:
        models.Profile.objects.create(
            first_name=instance.service_title,
            last_name=instance.service_description,
            phone_number=instance.phone_number,
            age=instance.age,
            gender=instance.gender
        )

@receiver(post_delete, sender=models.Favorites)
def favorite_bool(sender, instance, **kwargs):
    if instance.favorite_bool == False:
        Favourites.objects.get(user=instance.user).delete()