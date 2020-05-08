from django.db import models
from django.contrib.auth.models import User

class Badge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_login = models.BooleanField(default=False)
    completed_one_challenge = models.BooleanField(default=False)
    completed_five_challenges = models.BooleanField(default=False)
    completed_twenty_challenges = models.BooleanField(default=False)
    completed_fifty_challenges = models.BooleanField(default=False)
    completed_one_hundred_challenges = models.BooleanField(default=False)
    started_one_challenge = models.BooleanField(default=False)
    started_five_challenges = models.BooleanField(default=False)
    started_twenty_challenges = models.BooleanField(default=False)
    started_fifty_challenges = models.BooleanField(default=False)
    started_one_hundred_challenges = models.BooleanField(default=False)
