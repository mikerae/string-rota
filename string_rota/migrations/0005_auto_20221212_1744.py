# Generated by Django 3.2.3 on 2022-12-12 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0004_projectrepertoire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectrepertoire',
            name='repertoire',
        ),
        migrations.AddField(
            model_name='projectrepertoire',
            name='repertoire',
            field=models.ManyToManyField(to='string_rota.Repertoire'),
        ),
    ]
