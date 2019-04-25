# Generated by Django 2.2 on 2019-04-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieList', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieblock',
            name='original_title',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='movieblock',
            name='video',
            field=models.BooleanField(default=False),
        ),
    ]
