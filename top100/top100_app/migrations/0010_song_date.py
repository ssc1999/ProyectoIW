# Generated by Django 3.1.2 on 2020-12-20 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100_app', '0009_auto_20201215_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
