from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

DEFAULT_EXAM_ID=1
class Challenge(models.Model):
    title = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=30, blank=True)
    topic = models.CharField(max_length=30, blank=False, help_text='Please choose a topic for you challenge (Education, Law, Science, Medicine, IT, etc.)')
    short_description = models.CharField(max_length=500, blank=False, help_text='Please provide a short description of the challenge.')
    number_of_checks = models.IntegerField(blank=False, default=0, help_text='How many reviews do you want this challenge to go through?')
    agreed_number_of_checks = models.IntegerField(blank=False, default=0)
    completed_number_of_checks = models.IntegerField(blank=False, default=0)
    level = models.CharField(max_length=30, blank=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False, blank=False, help_text='Please provide a deadline for the reviews.')
    challenge_starter = models.ForeignKey(User, related_name="challenge_starter", blank=True, on_delete=models.CASCADE, default=DEFAULT_EXAM_ID)
    peer_reviewer = models.ManyToManyField(User, related_name="peer_reviewer", blank=True)
    completed_peer_reviewer = models.ManyToManyField(User, related_name="completed_peer_reviewer", blank=True)
    challenge_text = models.TextField(blank=False)
    auto_check_text = models.TextField(blank=True)
    peer_review_text = models.TextField(blank=True)
    notes = models.TextField(blank=True, help_text='Leave any additional comments here.')
    date_created = models.DateField(blank=False, default=datetime.date.today)
    date_accepted = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=datetime.date.today)
    date_completed = models.DateField(auto_now_add=False, auto_now=False, blank=True, default=datetime.date.today)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return self.title
