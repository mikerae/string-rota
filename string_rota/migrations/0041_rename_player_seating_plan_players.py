# Generated by Django 3.2.3 on 2022-12-22 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0040_rename_player_project_players'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seating_plan',
            old_name='player',
            new_name='players',
        ),
    ]