from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=True)
    level = models.CharField(max_length=30, blank=True)
    photo = models.ImageField(upload_to='images/')
    peer_review_points = models.PositiveIntegerField(blank=True, default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Level(models.Model):
    level = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.title
