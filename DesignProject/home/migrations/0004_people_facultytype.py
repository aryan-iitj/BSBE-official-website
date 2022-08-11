# Generated by Django 3.2 on 2022-01-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='FacultyType',
            field=models.CharField(blank=True, choices=[('RegularFaculty', 'RegularFaculty'), ('YoungFacultyAssociates', 'YoungFacultyAssociates'), ('GuestFaculty', 'GuestFaculty')], max_length=40),
        ),
    ]