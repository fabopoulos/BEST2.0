# Generated by Django 2.0 on 2017-12-19 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BestApp', '0006_auto_20171219_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='output',
            old_name='projet',
            new_name='project',
        ),
    ]
