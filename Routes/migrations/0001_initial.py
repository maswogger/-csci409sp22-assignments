# Generated by Django 4.1.5 on 2023-02-24 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline_name', models.CharField(max_length=100)),
                ('airline_code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField()),
                ('departure_city', models.CharField(max_length=50)),
                ('arrival_city', models.CharField(max_length=50)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('airline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Routes.airline')),
            ],
        ),
    ]
