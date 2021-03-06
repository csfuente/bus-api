# Generated by Django 3.1.6 on 2021-02-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=6)),
                ('asientos', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('rut', models.IntegerField()),
                ('cv', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Chofer',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='control.persona')),
            ],
            bases=('control.persona',),
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='control.persona')),
                ('nBoleta', models.PositiveIntegerField()),
            ],
            bases=('control.persona',),
        ),
        migrations.CreateModel(
            name='Trayecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.DateTimeField()),
                ('horaFin', models.DateTimeField()),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.bus')),
                ('chofer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.chofer')),
            ],
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.PositiveIntegerField()),
                ('trayecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.trayecto')),
                ('pasajero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.pasajero')),
            ],
        ),
    ]
