# Generated by Django 3.0.5 on 2020-04-18 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_auto_20200419_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='start_date',
        ),
    ]
