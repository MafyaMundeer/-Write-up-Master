# Generated by Django 2.0.9 on 2018-12-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_person_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]