from django import forms

class ClientesForms(forms.Form):
    nombre = forms.CharField(max_length=100)
    correo = forms.EmailField()
    telefono = forms.IntegerField()

class ReservasForms(forms.Form):
    cliente_nombre = forms.CharField(max_length=100)
    cliente_correo = forms.EmailField()
    cliente_telefono = forms.IntegerField()
    fecha_reserva = forms.DateField()
    hora_reserva = forms.TimeField()
    numero_personas = forms.IntegerField(min_value=1)

    