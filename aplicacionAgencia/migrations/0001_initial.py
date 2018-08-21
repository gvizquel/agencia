# Generated by Django 2.0.8 on 2018-08-21 02:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=255)),
                ('destino', models.CharField(max_length=255)),
                ('plaza', models.IntegerField()),
                ('precio', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Viajes',
                'db_table': 'viaje',
                'verbose_name': 'Viaje',
            },
        ),
        migrations.CreateModel(
            name='Viajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido')),
                ('letra_cedula_identidad', models.CharField(choices=[('V', 'V'), ('E', 'E')], default='V', max_length=1, verbose_name='Letra C.I.')),
                ('cedula_identidad', models.IntegerField(db_index=True, verbose_name='Cédula de Identidad')),
                ('direccion', ckeditor.fields.RichTextField()),
                ('telefono', models.CharField(max_length=255, verbose_name='Teléfono Local')),
            ],
            options={
                'verbose_name_plural': 'Viajeros',
                'db_table': 'viajero',
                'verbose_name': 'Viajero',
            },
        ),
    ]