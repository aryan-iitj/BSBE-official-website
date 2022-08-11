# Generated by Django 3.2 on 2022-02-04 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_faculty_advisors_facultytype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty_advisors',
            old_name='imgtitle',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='faculty_advisors',
            name='imgdesc',
        ),
        migrations.AddField(
            model_name='faculty_advisors',
            name='designation',
            field=models.CharField(blank=True, max_length=700),
        ),
        migrations.AddField(
            model_name='faculty_advisors',
            name='domain',
            field=models.CharField(blank=True, max_length=900),
        ),
        migrations.AddField(
            model_name='faculty_advisors',
            name='education',
            field=models.CharField(blank=True, max_length=700),
        ),
        migrations.AddField(
            model_name='faculty_advisors',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='faculty_advisors',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=16, unique=True, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]