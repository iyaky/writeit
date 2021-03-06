# Generated by Django 3.0.5 on 2020-05-08 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notification', '0002_auto_20200508_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.AddField(
            model_name='notification',
            name='from_user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notification_from_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='to_user',
            field=models.ManyToManyField(default=1, related_name='notification_to_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notification_type', to='notification.NotificationType'),
        ),
    ]
