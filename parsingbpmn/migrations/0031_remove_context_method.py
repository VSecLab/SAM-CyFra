# Generated by Django 3.1.5 on 2021-02-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0030_auto_20210223_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='context',
            name='method',
        ),
    ]
