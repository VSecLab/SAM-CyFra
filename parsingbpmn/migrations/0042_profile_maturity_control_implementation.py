# Generated by Django 3.1.5 on 2021-03-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0041_threat_has_family'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_maturity_control',
            name='implementation',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]