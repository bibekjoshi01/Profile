# Generated by Django 4.1.3 on 2022-11-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_about_profile_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='stack_url',
            field=models.URLField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, max_length=500),
        ),
    ]
