# Generated by Django 3.2.3 on 2022-12-20 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0035_alter_project_seating_plan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player_project',
            old_name='player_id',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='player_project',
            old_name='project_id',
            new_name='project',
        ),
    ]