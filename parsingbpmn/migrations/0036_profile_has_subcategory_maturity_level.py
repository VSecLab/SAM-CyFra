# Generated by Django 3.1.5 on 2021-03-04 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0035_remove_profile_has_subcategory_maturity_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_has_subcategory',
            name='maturity_level',
            field=models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.maturity_level'),
        ),
    ]