# Generated by Django 3.0.4 on 2020-05-11 02:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('family_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(default=None, verbose_name='Birth date')),
                ('nationality', models.CharField(max_length=100)),
                ('Poster', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='0', max_length=100)),
                ('release_date', models.DateField(default=datetime.datetime.now, verbose_name='release date: ')),
                ('Genre', models.CharField(max_length=100)),
                ('Poster', models.ImageField(height_field=250, upload_to='')),
                ('actor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='core.Actor', verbose_name='Actor')),
            ],
        ),
    ]
