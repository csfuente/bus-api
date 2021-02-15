from django.db.models import Count

from control.models import Chofer, Pasajero, Bus, Trayecto, Asiento, Horario
from control.serializers import ChoferSerializer, PasajeroSerializer, BusSerializer, TrayectoSerializer, AsientoSerializer, HorarioSerializer
from rest_framework import viewsets
import django_filters.rest_framework


class ChoferViewSet(viewsets.ModelViewSet):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer


class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class TrayectoViewSet(viewsets.ModelViewSet):
    queryset = Trayecto.objects.all()
    serializer_class = TrayectoSerializer


class AsientoViewSet(viewsets.ModelViewSet):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['horario']


class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['trayecto']

    def get_queryset(self):
        gt = self.request.GET.get('capacidad__gt')
        if gt:
            cumplen = list()
            asientos = Asiento.objects.exclude(pasajero=None).values('horario').order_by('horario').annotate(count=Count('horario'))
            for asiento in asientos:
                if asiento['count'] * 10 >= float(gt):
                    cumplen.append(asiento['horario'])
            return self.queryset.filter(id__in=cumplen)
        return self.queryset
