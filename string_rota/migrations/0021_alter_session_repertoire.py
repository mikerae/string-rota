# Generated by Django 3.2.3 on 2022-12-20 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0020_auto_20221220_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='repertoire',
            field=models.ManyToManyField(to='string_rota.Repertoire'),
        ),
    ]