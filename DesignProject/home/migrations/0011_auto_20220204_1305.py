# Generated by Django 3.2 on 2022-02-04 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20220204_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faculty_advisors',
            old_name='designation',
            new_name='imgdesc',
        ),
        migrations.RenameField(
            model_name='faculty_advisors',
            old_name='name1',
            new_name='imgtitle',
        ),
        migrations.RemoveField(
            model_name='faculty_advisors',
            name='domain',
        ),
        migrations.RemoveField(
            model_name='faculty_advisors',
            name='education',
        ),
        migrations.RemoveField(
            model_name='faculty_advisors',
            name='email',
        ),
        migrations.RemoveField(
            model_name='faculty_advisors',
            name='phoneNumber',
        ),
    ]
