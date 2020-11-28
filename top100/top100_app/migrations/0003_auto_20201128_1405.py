# Generated by Django 3.1.3 on 2020-11-28 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('top100_app', '0002_auto_20201128_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=13),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('repros', models.IntegerField(max_length=100000000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='top100_app.author')),
                ('gender', models.ManyToManyField(to='top100_app.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('repros', models.IntegerField(max_length=100000000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='top100_app.author')),
                ('gender', models.ManyToManyField(to='top100_app.Gender')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='top100_app.song')),
            ],
        ),
    ]