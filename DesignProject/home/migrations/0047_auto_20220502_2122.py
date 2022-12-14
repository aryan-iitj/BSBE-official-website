# Generated by Django 3.2 on 2022-05-02 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20220423_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='awardslist',
            name='FullName',
            field=models.CharField(default='Full name', max_length=200),
        ),
        migrations.AddField(
            model_name='publicationlist',
            name='FullName',
            field=models.CharField(default='Full name', max_length=200),
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 5, 2)),
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Time',
            field=models.TimeField(default=datetime.time(21, 22, 16, 47384)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 5, 2)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Time',
            field=models.TimeField(default=datetime.time(21, 22, 16, 47384)),
        ),
    ]
