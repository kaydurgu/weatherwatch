# Generated by Django 5.0.6 on 2024-06-03 00:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('thermometer', 'Thermometer'), ('hygrometer', 'Hygrometer'), ('barometer', 'Barometer'), ('wind_vane:', 'Wind Vane'), ('snow_gauge:', 'Snow Gauge')], default='thermometer', max_length=20)),
                ('model', models.CharField(max_length=100)),
                ('region', models.CharField(choices=[('batken', 'Batken'), ('bishkek', 'Bishkek'), ('osh', 'Osh')], default='bishkek', max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('installation_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('maintenance', 'Under Maintenance')], default='active', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('responsible', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('humidity', models.FloatField(blank=True, null=True)),
                ('pressure', models.FloatField(blank=True, null=True)),
                ('wind_speed', models.FloatField(blank=True, null=True)),
                ('wind_direction', models.CharField(blank=True, max_length=250, null=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='Sensors.sensor')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('last_timestamp', models.DateTimeField(auto_now=True)),
                ('warning_notes', models.TextField(blank=True, null=True)),
                ('severity', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low'), ('ok', 'Ok')], default='ok', max_length=10)),
                ('last_timecheckedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='Sensors.sensor')),
            ],
        ),
    ]
