# Generated by Django 3.2 on 2022-04-23 05:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20220423_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NameFaculty', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=80)),
                ('RollNo', models.CharField(max_length=80)),
                ('Category', models.CharField(max_length=100)),
                ('SupervisiorI', models.CharField(max_length=100)),
                ('SupervisiorII', models.CharField(blank=True, max_length=100)),
                ('ProjectType', models.CharField(choices=[('BTP', 'BTP'), ('MTech', 'MTech'), ('MTech', 'MTech'), ('MTech-Phd', 'MTech-Phd'), ('Phd', 'Phd')], max_length=60)),
                ('SRCMemberI', models.CharField(blank=True, max_length=100)),
                ('SRCMemberII', models.CharField(blank=True, max_length=100)),
                ('SRCMemberIII', models.CharField(blank=True, max_length=100)),
                ('ProjectTitle', models.CharField(max_length=100)),
                ('ThesisSubmission', models.CharField(max_length=100)),
                ('Defence', models.CharField(max_length=100)),
                ('Remarks', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='upcomingstudentppt',
            name='Time',
            field=models.TimeField(default=datetime.time(10, 37, 8, 876627)),
        ),
        migrations.AlterField(
            model_name='upcomingwebinar',
            name='Time',
            field=models.TimeField(default=datetime.time(10, 37, 8, 875627)),
        ),
    ]
