# Generated by Django 3.1.5 on 2021-02-10 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0008_category_function'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Threat_has_subcategory',
            new_name='is_a_requirement_for_mitigation',
        ),
    ]