# Generated by Django 4.2.19 on 2025-02-27 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_hydroponicsystem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('hydroponic_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systems.hydroponicsystem')),
            ],
        ),
    ]
