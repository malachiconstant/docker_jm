# Generated by Django 2.2 on 2019-04-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieList', '0002_auto_20190423_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieblock',
            name='adult',
            field=models.BooleanField(default=False, help_text='check box if movie is for adults only'),
        ),
    ]
