from django.db import models
from django.contrib.auth.models import User

class Badge(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_login = models.BooleanField(default=False)
    # completed_one_challenge = models.BooleanField(default=False)
    # completed_five_challenges = models.BooleanField(default=False)
    # completed_twenty_challenges = models.BooleanField(default=False)
    # completed_fifty_challenges = models.BooleanField(default=False)
    # completed_one_hundred_challenges = models.BooleanField(default=False)
    # started_one_challenge = models.BooleanField(default=False)
    # started_five_challenges = models.BooleanField(default=False)
    # started_twenty_challenges = models.BooleanField(default=False)
    # started_fifty_challenges = models.BooleanField(default=False)
    # started_one_hundred_challenges = models.BooleanField(default=False)
    badge_users = models.ManyToManyField(User, related_name="badge_users", blank=True)
    badge_name = models.CharField(max_length=50, blank=False, default="")
    badge_icon = models.ImageField(upload_to='images/badges/', default='/static/badges_default/badge_default.png')
    badge_icon_black = models.ImageField(upload_to='images/badges_black/', default='/static/badges_default/badge_default.png')

    def __str__(self):
        return self.badge_name
