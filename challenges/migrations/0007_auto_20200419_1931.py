# Generated by Django 3.0.5 on 2020-04-19 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0006_auto_20200419_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='auto_check_text',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='challenge',
            name='peer_review_text',
            field=models.TextField(blank=True),
        ),
    ]
