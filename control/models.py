from django.db import models


class Bus(models.Model):
    patente = models.CharField(max_length=6)
    asientos = models.IntegerField(default=10)

    def __unicode__(self):
        return self.patente


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    rut = models.IntegerField()
    cv = models.CharField(max_length=1)

    def __unicode__(self):
        return self.nombre


class Chofer(Persona):
    pass


class Pasajero(Persona):
    pass


class Trayecto(models.Model):
    nombre = models.CharField(max_length=60)


class Horario(models.Model):
    trayecto = models.ForeignKey(Trayecto, on_delete=models.CASCADE)
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField()
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    chofer = models.ForeignKey(Chofer, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        super(Horario, self).save(*args, **kwargs)
        if not len(Asiento.objects.filter(horario=self)):
            for i in range(self.bus.asientos):
                Asiento(numero=i + 1, horario=self).save()


class Asiento(models.Model):
    numero = models.PositiveIntegerField()
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    pasajero = models.ForeignKey(Pasajero, on_delete=models.SET_NULL, null=True, blank=True)

    def __unicode__(self):
        return f'{str(self.trayecto)} - {self.numero} - {self.pasajero}'
