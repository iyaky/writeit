# Generated by Django 3.0.5 on 2020-05-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0019_challenge_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='uploaded_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
