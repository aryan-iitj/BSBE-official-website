# Generated by Django 3.2 on 2022-04-22 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0042_auto_20220414_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameFaculty', models.CharField(max_length=50)),
                ('Faculty', models.CharField(max_length=80)),
                ('ProjectNo', models.IntegerField()),
                ('ProjectTitle', models.CharField(max_length=100)),
                ('FundingAgency', models.CharField(max_length=200)),
                ('SanctionedAmount', models.CharField(max_length=50)),
                ('Duration', models.CharField(max_length=50)),
                ('Status', models.CharField(max_length=50)),
                ('FinancialYear', models.IntegerField()),
                ('Details', models.CharField(default='-', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 4, 23)),
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Time',
            field=models.TimeField(default=datetime.time(1, 7, 51, 496531)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Date',
            field=models.DateField(default=datetime.date(2022, 4, 23)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Time',
            field=models.TimeField(default=datetime.time(1, 7, 51, 495535)),
        ),
    ]
