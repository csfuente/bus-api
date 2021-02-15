from control.models import Chofer, Pasajero, Bus, Trayecto, Asiento, Horario
from rest_framework import serializers


class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = ['id', 'nombre', 'rut', 'cv']


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ['id', 'nombre', 'rut', 'cv']


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'patente', 'asientos']


class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = ['id', 'numero', 'horario', 'pasajero']


class TrayectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trayecto
        fields = ['id', 'nombre']


class HorarioSerializer(serializers.ModelSerializer):
    capacidad = serializers.SerializerMethodField()

    class Meta:
        model = Horario
        fields = ['id', 'trayecto', 'horaInicio', 'horaFin', 'bus', 'chofer', 'capacidad']
        read_only_fields = ('capacidad',)

    def get_capacidad(self, obj):
        asientos = Asiento.objects.filter(horario=obj)
        return f'{(len(asientos.exclude(pasajero=None)) / len(asientos)) * 100} %'
