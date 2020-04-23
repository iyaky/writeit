# Generated by Django 3.0.5 on 2020-04-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0008_challenge_peer_reviewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_accepted', models.DateField(auto_now=True)),
                ('date_completed', models.DateField(auto_now_add=True)),
                ('text_before_review', models.TextField()),
                ('text_after_review', models.TextField(blank=True)),
                ('challenge', models.ManyToManyField(to='challenges.Challenge')),
            ],
        ),
    ]