# Generated by Django 3.2.3 on 2022-12-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0016_project_repertoire_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.TimeField(),
        ),
    ]