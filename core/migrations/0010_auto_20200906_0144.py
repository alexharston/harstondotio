# Generated by Django 2.1.14 on 2020-09-06 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20200906_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
