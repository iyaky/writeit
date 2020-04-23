from django.db import models
from django.contrib.auth.models import User

class Badge(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_login = models.BooleanField(default=False)
    one_challenge = models.BooleanField(default=False)
    five_challenges = models.BooleanField(default=False)
    twenty_challenges = models.BooleanField(default=False)
    fifty_challenges = models.BooleanField(default=False)
    one_hundred_challenges = models.BooleanField(default=False)
    two_day_streak = models.BooleanField(default=False)
    seven_days_streak = models.BooleanField(default=False)
    two_weeks_streak = models.BooleanField(default=False)
    one_month_streak = models.BooleanField(default=False)
