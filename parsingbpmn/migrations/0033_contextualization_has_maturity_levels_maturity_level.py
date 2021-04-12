# Generated by Django 3.1.5 on 2021-03-04 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0032_remove_profile_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maturity_level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Maturity_level',
                'verbose_name_plural': 'maturity_levels',
            },
        ),
        migrations.CreateModel(
            name='contextualization_has_maturity_levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maturity_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.maturity_level')),
                ('subcategory_contextualization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parsingbpmn.contextualization')),
            ],
        ),
    ]
