# Generated by Django 2.1.14 on 2020-09-06 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
    ]
