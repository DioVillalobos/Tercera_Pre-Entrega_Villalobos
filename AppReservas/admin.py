from django.contrib import admin
from .models import Cliente, Reserva, Mesa

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Reserva)
admin.site.register(Mesa)
