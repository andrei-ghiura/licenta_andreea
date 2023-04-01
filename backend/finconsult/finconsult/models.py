from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Meeting(models.Model):
    consultant = models.OneToOneField(User, on_delete=models.CASCADE)
    client = models.OneToOneField(
        User, blank=True, on_delete=models.CASCADE, related_name='client')
    newcommer = models.BooleanField(default=False)
    nc_name = models.TextField(max_length=100, blank=True)
    nc_birth_date = models.DateField(null=True, blank=True)
    nc_phone = models.TextField(max_length=500, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Profile(models.Model):

    class Roles(models.TextChoices):
        CONSULTANT = 'CO', _('Consultant')
        ADMIN = 'AD', _('Admin')
        CLIENT = 'CL', _('Client')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    position = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.CONSULTANT,
    )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()