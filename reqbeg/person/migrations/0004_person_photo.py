# Generated by Django 2.0.9 on 2018-12-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_auto_20181228_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
