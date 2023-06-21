from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Meeting(models.Model):
    # add a meeting id field that auto increments
    id = models.AutoField(primary_key=True)
    consultant = models.ForeignKey(
        User, blank=True, on_delete=models.CASCADE, related_name='consultant')
    client = models.OneToOneField(
        User, blank=True, on_delete=models.CASCADE, related_name='client')
    notes = models.TextField(max_length=500, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    location = models.TextField(max_length=500, blank=True)
    title = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.id)


class Profile(models.Model):

    class Roles(models.TextChoices):
        CONSULTANT = 'CO', _('Consultant')
        ADMIN = 'AD', _('Admin')
        CLIENT = 'CL', _('Client')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.TextField(max_length=500, blank=True)
    position = models.CharField(
        max_length=2,
        choices=Roles.choices,
        default=Roles.CONSULTANT,
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
