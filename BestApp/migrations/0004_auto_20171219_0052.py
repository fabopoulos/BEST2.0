# Generated by Django 2.0 on 2017-12-19 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BestApp', '0003_auto_20171219_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='targer',
            new_name='target',
        ),
    ]
