# Generated by Django 3.0.5 on 2020-05-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0024_auto_20200505_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='result_file',
            field=models.FileField(blank=True, upload_to='documents/results'),
        ),
    ]