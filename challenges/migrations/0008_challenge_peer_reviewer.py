# Generated by Django 3.0.5 on 2020-04-19 16:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0007_auto_20200419_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='peer_reviewer',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]