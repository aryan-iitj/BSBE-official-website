# Generated by Django 3.2 on 2022-01-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_newsandevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgtitle', models.CharField(max_length=100)),
                ('imgdesc', models.CharField(max_length=700)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
