# Generated by Django 3.0.5 on 2020-04-23 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0018_challenge_completed_peer_reviewer'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='feedback',
            field=models.TextField(blank=True),
        ),
    ]