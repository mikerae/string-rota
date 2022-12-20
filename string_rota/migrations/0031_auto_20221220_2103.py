# Generated by Django 3.2.3 on 2022-12-20 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('string_rota', '0030_auto_20221220_1911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seating_plan',
            old_name='section_name',
            new_name='section',
        ),
        migrations.RemoveField(
            model_name='seating_plan',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='seating_plan',
            name='seating_position',
        ),
        migrations.RemoveField(
            model_name='seating_position',
            name='section',
        ),
        migrations.AddField(
            model_name='seating_plan',
            name='plan_status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Published')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='seating_position',
            name='seating_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='string_rota.seating_plan'),
        ),
    ]
