# Generated by Django 4.1.5 on 2023-01-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='approximate_waiting_time',
        ),
        migrations.RemoveField(
            model_name='token',
            name='current_token',
        ),
        migrations.AddField(
            model_name='token',
            name='is_served',
            field=models.BooleanField(default=False),
        ),
    ]
