# Generated by Django 3.1.2 on 2020-12-15 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100_app', '0007_genre_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.CharField(default='Description', max_length=500),
        ),
    ]
