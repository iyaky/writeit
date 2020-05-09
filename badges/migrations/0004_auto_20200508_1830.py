# Generated by Django 3.0.5 on 2020-05-08 15:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('badges', '0003_auto_20200504_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='completed_fifty_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='completed_five_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='completed_one_challenge',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='completed_one_hundred_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='completed_twenty_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='first_login',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='started_fifty_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='started_five_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='started_one_challenge',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='started_one_hundred_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='started_twenty_challenges',
        ),
        migrations.RemoveField(
            model_name='badge',
            name='user',
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_icon',
            field=models.ImageField(default='/static/badges_default/badge_default.png', upload_to='images/badges/'),
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_icon_black',
            field=models.ImageField(default='/static/badges_default/badge_default.png', upload_to='images/badges_black/'),
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_users',
            field=models.ManyToManyField(blank=True, related_name='badge_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
