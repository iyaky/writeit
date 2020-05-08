# Generated by Django 3.0.5 on 2020-05-07 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0027_auto_20200507_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='accepted_and_closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='challenge',
            name='opened_dispute',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='topic', to='challenges.ChallengeTopicName'),
        ),
    ]
