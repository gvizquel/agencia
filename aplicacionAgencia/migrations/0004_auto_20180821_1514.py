# Generated by Django 2.0.8 on 2018-08-21 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionAgencia', '0003_itinerario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerario',
            old_name='persona',
            new_name='viaje',
        ),
    ]