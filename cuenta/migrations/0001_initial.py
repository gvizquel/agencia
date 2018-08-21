# Generated by Django 2.0.8 on 2018-08-21 02:27

import cuenta.libSobreEscribirImagen
import cuenta.models
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password', models.CharField(max_length=128, verbose_name='Clave')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Último inicio de sesión:')),
                ('is_superuser', models.BooleanField(db_index=True, default=False, verbose_name='Super Administrador')),
                ('is_staff', models.BooleanField(db_index=True, default=False, verbose_name='Mantenimiento')),
                ('is_active', models.BooleanField(default=False, verbose_name='Activo')),
                ('username', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Nombre de usuario')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.CharField(db_index=True, max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('email_secundario', models.CharField(blank=True, db_index=True, max_length=254, null=True, unique=True, verbose_name='Correo Secundario')),
                ('letra_cedula_identidad', models.CharField(blank=True, choices=[('V', 'V'), ('E', 'E')], default='V', max_length=1, null=True, verbose_name='Letra C.I.')),
                ('cedula_identidad', models.IntegerField(blank=True, db_index=True, null=True, verbose_name='Cédula de Identidad')),
                ('otros_nombres', models.CharField(blank=True, max_length=90, null=True, verbose_name='Otros Nombres')),
                ('otros_apellidos', models.CharField(blank=True, max_length=255, null=True, verbose_name='Otros Apellidos')),
                ('telefono', models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono Local')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Teléfono Celular')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='FaceBook')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('sexo', models.CharField(blank=True, choices=[('F', 'FEMENINO'), ('M', 'MASCULINO')], max_length=255, null=True)),
                ('avatar', models.ImageField(blank=True, default='avatar/default_avatar.png', max_length=255, null=True, storage=cuenta.libSobreEscribirImagen.SobreEscribirAvatar(), upload_to=cuenta.models.image_path)),
                ('twitter', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Personas',
                'verbose_name': 'Persona',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
