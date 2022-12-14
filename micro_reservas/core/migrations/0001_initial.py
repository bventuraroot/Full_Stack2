# Generated by Django 3.2.16 on 2022-10-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('bookings_id', models.AutoField(primary_key=True, serialize=False)),
                ('bookings_reservation_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'bookings',
                'verbose_name_plural': 'bookings',
                'db_table': 'bookings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courts',
            fields=[
                ('courts_id', models.AutoField(primary_key=True, serialize=False)),
                ('courts_name', models.CharField(max_length=90, unique=True)),
                ('courts_descripcion', models.TextField(blank=True, null=True)),
                ('courts_location', models.CharField(blank=True, max_length=90, null=True)),
                ('courts_picture', models.CharField(blank=True, max_length=190, null=True)),
                ('courts_state', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'courts',
                'verbose_name_plural': 'courts',
                'db_table': 'courts',
                'ordering': ['courts_id'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Frecuency',
            fields=[
                ('frecuency_id', models.AutoField(primary_key=True, serialize=False)),
                ('frecuency', models.CharField(blank=True, max_length=90, null=True)),
                ('frecuency_state', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'frecuency',
                'verbose_name_plural': 'frecuency',
                'db_table': 'frecuency',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('partners_id', models.AutoField(primary_key=True, serialize=False)),
                ('partners_code', models.CharField(blank=True, max_length=9, null=True)),
                ('partners_fist_name', models.CharField(blank=True, max_length=90, null=True)),
                ('partners_last_name', models.CharField(blank=True, max_length=90, null=True)),
                ('partners_full_name', models.CharField(blank=True, max_length=190, null=True)),
                ('partners_nick_name', models.CharField(blank=True, max_length=90, null=True)),
                ('partners_nationality', models.CharField(blank=True, max_length=90, null=True)),
                ('partners_picture', models.CharField(blank=True, max_length=190, null=True)),
                ('partners_document_type', models.CharField(blank=True, choices=[('DNI', 'DNI'), ('PASAPORTE', 'PASAPORTE'), ('VISA', 'VISA')], max_length=90, null=True)),
                ('partners_nro_document', models.CharField(blank=True, max_length=10, null=True)),
                ('partners_address', models.CharField(blank=True, max_length=190, null=True)),
                ('partners_phone', models.CharField(blank=True, max_length=10, null=True)),
                ('partners_birth_date', models.DateField(blank=True, null=True)),
                ('partners_state', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'partners',
                'verbose_name_plural': 'partners',
                'db_table': 'partners',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('states_id', models.AutoField(primary_key=True, serialize=False)),
                ('states_name', models.CharField(blank=True, max_length=90, null=True)),
                ('states_state', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'states',
                'verbose_name_plural': 'states',
                'db_table': 'states',
                'managed': False,
            },
        ),
    ]
