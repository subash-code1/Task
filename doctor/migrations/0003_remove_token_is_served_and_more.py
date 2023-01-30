# Generated by Django 4.1.5 on 2023-01-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_remove_token_approximate_waiting_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='is_served',
        ),
        migrations.AddField(
            model_name='token',
            name='approximate_waiting_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='token',
            name='current_token',
            field=models.IntegerField(default=None),
        ),
    ]