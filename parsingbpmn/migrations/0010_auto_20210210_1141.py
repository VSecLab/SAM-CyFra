# Generated by Django 3.1.5 on 2021-02-10 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0009_auto_20210210_1140'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='subcategory_has_control',
            new_name='Subcategory_is_implemented_through_control',
        ),
    ]