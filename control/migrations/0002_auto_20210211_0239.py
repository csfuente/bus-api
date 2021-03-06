# Generated by Django 3.1.6 on 2021-02-11 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asiento',
            name='trayecto',
        ),
        migrations.RemoveField(
            model_name='trayecto',
            name='bus',
        ),
        migrations.RemoveField(
            model_name='trayecto',
            name='chofer',
        ),
        migrations.RemoveField(
            model_name='trayecto',
            name='horaFin',
        ),
        migrations.RemoveField(
            model_name='trayecto',
            name='horaInicio',
        ),
        migrations.AddField(
            model_name='trayecto',
            name='nombre',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.DateTimeField()),
                ('horaFin', models.DateTimeField()),
                ('bus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.bus')),
                ('chofer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='control.chofer')),
                ('trayecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.trayecto')),
            ],
        ),
        migrations.AddField(
            model_name='asiento',
            name='horario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='control.horario'),
            preserve_default=False,
        ),
    ]
