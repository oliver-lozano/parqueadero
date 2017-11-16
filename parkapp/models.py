from django.db import models

class empleados(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.TextField(blank=False, default='')
    apellidos = models.TextField(blank=False, default='')
    telefono = models.TextField(blank=False, default='')
    usuario = models.TextField(blank=False, default='', unique='True')
    clave = models.TextField(blank=False, default='')

TIPOSVEHICULOS=(
('CA','Carro'),
('MO','Moto'),
('BI','Bicicleta'),
)

class tipovehiculo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=2, choices=TIPOSVEHICULOS)
    tarifa = models.IntegerField()
    posiciones = models.IntegerField()

class ticket(models.Model):
    id = models.AutoField(primary_key=True)
    fechain = models.DateTimeField()
    fechaout = models.DateTimeField()
    total = models.IntegerField()
    estado = models.BooleanField(default=False)
    vehiculos = models.ForeignKey('vehiculos')

class vehiculos(models.Model):
    id = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=7, default='')
    tipovehiculo = models.ForeignKey('tipovehiculo')
