# Generated by Django 3.0.4 on 2020-05-11 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200511_0221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='Poster',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='film',
            name='Poster',
            field=models.ImageField(upload_to=''),
        ),
    ]
