# Generated by Django 3.2.3 on 2022-12-12 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0002_repertoire'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repertoire',
            old_name='intrumentation',
            new_name='instrumentation',
        ),
    ]