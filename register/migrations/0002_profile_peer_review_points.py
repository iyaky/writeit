# Generated by Django 3.0.5 on 2020-05-06 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='peer_review_points',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
