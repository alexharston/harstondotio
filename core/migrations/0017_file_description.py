# Generated by Django 3.0.9 on 2020-10-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]