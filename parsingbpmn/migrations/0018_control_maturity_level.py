# Generated by Django 3.1.5 on 2021-02-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0017_auto_20210210_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='control',
            name='maturity_level',
            field=models.CharField(default='minimo', max_length=100),
        ),
    ]