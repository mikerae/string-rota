# Generated by Django 3.2.3 on 2022-12-20 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0031_auto_20221220_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='seating_plan',
            field=models.ManyToManyField(related_name='plan_seating', to='string_rota.Seating_Plan'),
        ),
    ]
