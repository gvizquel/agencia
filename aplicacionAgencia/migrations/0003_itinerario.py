# Generated by Django 2.0.8 on 2018-08-21 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionAgencia', '0002_auto_20180820_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salida', models.DateField()),
                ('retorno', models.DateField()),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacionAgencia.Viaje')),
                ('viajero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='aplicacionAgencia.Viajero')),
            ],
            options={
                'db_table': 'itinerario',
            },
        ),
    ]
