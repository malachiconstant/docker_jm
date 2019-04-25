# Generated by Django 2.2 on 2019-04-25 15:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieList', '0002_auto_20190425_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieblock',
            name='genre_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(blank=True, default=0), default=list, size=8),
        ),
    ]
