from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

DEFAULT_EXAM_ID=1
DEFAULT_USER_ID=27

class ChallengeTopicName(models.Model):

    topic_name = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.topic_name


class Challenge(models.Model):
    title = models.CharField(max_length=30, blank=False)
    status = models.CharField(max_length=30, blank=True)
    topic = models.ForeignKey(ChallengeTopicName, related_name="topic", blank=False, on_delete=models.SET_DEFAULT, default=DEFAULT_EXAM_ID)
    short_description = models.TextField(blank=False, help_text='Please provide a short description of the challenge.')
    number_of_checks = models.PositiveSmallIntegerField(blank=False, default=0, help_text='How many reviews do you want this challenge to go through?')
    agreed_number_of_checks = models.PositiveSmallIntegerField(blank=False, default=0)
    completed_number_of_checks = models.PositiveSmallIntegerField(blank=False, default=0)
    level = models.CharField(max_length=30, blank=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False, blank=False, help_text='Please provide a deadline for the reviews.')
    challenge_starter = models.ForeignKey(User, related_name="challenge_starter", blank=True, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
    peer_reviewer = models.ManyToManyField(User, related_name="peer_reviewer", blank=True)
    completed_peer_reviewer = models.ManyToManyField(User, related_name="completed_peer_reviewer", blank=True)
    uploaded_file = models.FileField(upload_to='documents/', blank=True)
    result_file = models.FileField(upload_to='documents/results', blank=True)
    file_challenge = models.BooleanField(default=False, blank=False)
    challenge_text = models.TextField(blank=True)
    auto_check_text = models.TextField(blank=True)
    peer_review_text = models.TextField(blank=True)
    notes = models.TextField(blank=True, help_text='Leave any additional comments here.')
    date_created = models.DateField(blank=False, default=datetime.date.today)
    date_accepted = models.DateField(auto_now=False, auto_now_add=False, blank=True, default=datetime.date.today)
    date_completed = models.DateField(auto_now_add=False, auto_now=False, blank=True, default=datetime.date.today)
    completed_other_challenge = models.BooleanField(default=False, blank=False)
    feedback = models.TextField(blank=True)
    accepted_and_closed = models.BooleanField(default=False, blank=False)
    opened_dispute = models.BooleanField(default=False, blank=False)


    def __str__(self):
        return self.title
