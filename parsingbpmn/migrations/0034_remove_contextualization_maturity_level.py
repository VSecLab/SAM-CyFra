# Generated by Django 3.1.5 on 2021-03-04 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0033_contextualization_has_maturity_levels_maturity_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contextualization',
            name='maturity_level',
        ),
    ]
