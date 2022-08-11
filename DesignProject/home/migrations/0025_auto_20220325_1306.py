# Generated by Django 3.2 on 2022-03-25 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_researchareas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.TextField()),
                ('Investigators', models.TextField()),
                ('FundingAgencies', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='ResearchAreas',
        ),
    ]