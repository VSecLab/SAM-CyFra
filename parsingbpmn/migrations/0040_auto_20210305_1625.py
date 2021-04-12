# Generated by Django 3.1.5 on 2021-03-05 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0039_remove_control_framework_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='family',
            name='source',
        ),
        migrations.AddField(
            model_name='family',
            name='framework_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.control_framework'),
        ),
    ]