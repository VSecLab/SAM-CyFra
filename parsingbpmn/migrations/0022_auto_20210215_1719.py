# Generated by Django 3.1.5 on 2021-02-15 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parsingbpmn', '0021_auto_20210215_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contextualization_and_profile',
            old_name='context',
            new_name='context_and_profile',
        ),
        migrations.RemoveField(
            model_name='profile_has_context',
            name='context_id',
        ),
        migrations.RemoveField(
            model_name='profile_has_context',
            name='profile_id',
        ),
        migrations.AddField(
            model_name='profile_has_context',
            name='context',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='contextualization', to='parsingbpmn.context_and_profile'),
        ),
        migrations.AddField(
            model_name='profile_has_context',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile_id', to='parsingbpmn.context_and_profile'),
        ),
    ]