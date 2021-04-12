# Generated by Django 3.1.5 on 2021-02-10 10:31

from django.db import migrations, models
import parsingbpmn.models


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0007_auto_20210210_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='function',
            field=models.CharField(choices=[('ID', 'Identify'), ('PR', 'Protect'), ('DE', 'Detect'), ('RS', 'Respond'), ('RC', 'Recover')], default=parsingbpmn.models.Category.FunctionStatus['IDENTIFY'], max_length=250, verbose_name='function'),
        ),
    ]
