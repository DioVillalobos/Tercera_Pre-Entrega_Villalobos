from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/', clientes, name ='clientes'),
    path('reservas/', reservas, name = 'reservas'),
    path('mesas/', mesas, name = 'mesas'),
    path("crear_mesa", crear_mesa),
    path("listar_mesas", listar_mesas),
    path("busqueda_reserva", busqueda_reserva, name ='busquedaReserva'),
    path("buscar/", buscar, name = 'buscar')
]