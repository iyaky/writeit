# Generated by Django 3.0.5 on 2020-05-08 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationtype',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
