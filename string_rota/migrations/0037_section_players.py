# Generated by Django 3.2.3 on 2022-12-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0036_auto_20221220_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='players',
            field=models.ManyToManyField(related_name='stg_section', to='string_rota.Player'),
        ),
    ]
