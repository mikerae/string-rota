# Generated by Django 3.2.3 on 2022-12-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0006_auto_20221216_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='section_name',
            field=models.CharField(max_length=11),
        ),
    ]