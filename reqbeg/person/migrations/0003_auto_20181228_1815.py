# Generated by Django 2.0.9 on 2018-12-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_person_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(max_length=30),
        ),
    ]
