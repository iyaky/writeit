from django.contrib import admin
from .models import NotificationType, Notification

admin.site.register(NotificationType)
admin.site.register(Notification)
# Register your models here.
