# Generated by Django 2.1.14 on 2020-09-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200906_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
