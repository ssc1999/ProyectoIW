# Generated by Django 3.1.3 on 2020-11-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100_app', '0003_auto_20201128_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='repros',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='song',
            name='repros',
            field=models.IntegerField(),
        ),
    ]
