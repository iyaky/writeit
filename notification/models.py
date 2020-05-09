from django.db import models
from django.contrib.auth.models import User
import datetime

DEFAULT_EXAM_ID=1
DEFAULT_CHALLENDE_ID=159

class NotificationType(models.Model):
    name = models.CharField(max_length=30, blank=True)
    not_text = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Notification(models.Model):
    to_user = models.ForeignKey(User, related_name="notification_to_user", blank=True, on_delete=models.CASCADE, default=DEFAULT_EXAM_ID)
    type = models.ForeignKey(NotificationType, related_name="notification_type", blank=True, on_delete=models.CASCADE, default=DEFAULT_EXAM_ID)
    notification_text = models.CharField(max_length=500, blank=True)
    read = models.BooleanField(default=False, blank=False)
    date_created = models.DateField(blank=False, default=datetime.date.today)
