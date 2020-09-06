# Generated by Django 2.1.14 on 2020-09-06 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200906_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='design',
            name='published_year',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(),
        ),
        migrations.AlterField(
            model_name='use',
            name='category',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='use',
            name='title',
            field=models.TextField(max_length=500),
        ),
    ]