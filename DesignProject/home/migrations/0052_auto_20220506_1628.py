# Generated by Django 3.2 on 2022-05-06 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0051_auto_20220506_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationlist',
            name='Title',
            field=models.CharField(max_length=400, unique=True),
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Time',
            field=models.TimeField(default=datetime.time(16, 28, 17, 797964)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Time',
            field=models.TimeField(default=datetime.time(16, 28, 17, 797964)),
        ),
    ]