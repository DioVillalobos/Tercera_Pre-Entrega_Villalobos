from django.core.exceptions import ValidationError #incorpora el ValidationError
from django.core.validators import MinValueValidator #incorpora el MinValueValidator
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.IntegerField()

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    numero_personas = models.IntegerField(validators=[MinValueValidator(1)]) #por lo que entendi, esta ultima parte sirve para establecer valores minimos en este atributo.

    def clean_numero_personas(self):
        numero_personas = self.numero_personas
        if numero_personas <= 0:
            raise ValidationError("El número de personas debe ser mayor que cero.") #por lo que entendi, es una especie de excepcion para manejar errores a la hora de introducir datos en formularios. "Raise" se usa para elevar la excepcion.
        return numero_personas

class Mesa(models.Model):
    numero = models.IntegerField()
    capacidad = models.IntegerField()
    disponibilidad_mesa = models.BooleanField(default=True)
    def __str__(self):
        return f"Mesa Numero {self.numero} - Capacidad {self.capacidad} Personas - Disponibilidad: {self.disponibilidad_mesa}"
    