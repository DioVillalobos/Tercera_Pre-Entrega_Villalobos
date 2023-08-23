from django.shortcuts import render
from django.http import HttpResponse
from .models import Mesa, Cliente, Reserva
from .forms import ClientesForms, ReservasForms

# Create your views here.

def crear_mesa(request):
    numero_mesa = 1
    capacidad_mesa = 2
    print("creando mesa")
    mesita = Mesa(numero=numero_mesa, capacidad=capacidad_mesa)
    mesita.save()
    respuesta = f"Mesa Creada - Numero de Mesa {mesita.numero} Capacidad {mesita.capacidad} Clientes"
    return HttpResponse(respuesta)
    
def listar_mesas(request):
    mesitas=Mesa.objects.all() #todos los objetos "Mesa"
    respuesta = ""
    for mesita in mesitas:
        respuesta+=f"Mesa {mesita.numero} con capacidad para {mesita.capacidad} Clientes<br>"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request, "AppReservas/inicio.html")

def clientes(request):
    if request.method == "POST":
        form=ClientesForms(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            correo=info["correo"]
            telefono=info["telefono"]
            cliente=Cliente(nombre=nombre, correo=correo, telefono=telefono)
            cliente.save()
            return render(request, "AppReservas/clientes.html", {"mensaje":"Cliente Registrado"})
        else:
            return render(request, "AppReservas/clientes.html", {"mensaje":"ERROR: Datos Invalidos"})
    else:
        formulario_cliente=ClientesForms()
    return render(request, "AppReservas/clientes.html", {"formulario":formulario_cliente})

def reservas(request):
    if request.method == "POST":
        form = ReservasForms(request.POST)
        if form.is_valid():
            cliente_nombre = form.cleaned_data["cliente_nombre"]
            cliente_correo = form.cleaned_data["cliente_correo"]
            cliente_telefono = form.cleaned_data["cliente_telefono"]
            fecha_reserva = form.cleaned_data["fecha_reserva"]
            hora_reserva = form.cleaned_data["hora_reserva"]
            numero_personas = form.cleaned_data["numero_personas"]

            cliente, created = Cliente.objects.get_or_create( nombre=cliente_nombre, defaults={"correo": cliente_correo, "telefono": cliente_telefono}) #aqui creo un nuevo cliente o puedo obtener los datos de uno existente
            reserva = Reserva(cliente=cliente, fecha_reserva=fecha_reserva, hora_reserva=hora_reserva, numero_personas=numero_personas) #creo una nueva reserva relacionada con el cliente
            reserva.save()
            return render(request, "AppReservas/reservas.html", {"mensaje": "Reserva Registrada"})
    else:
        formulario_reserva = ReservasForms()
    
    return render(request, "AppReservas/reservas.html", {"formulario": formulario_reserva})

def mesas(request):
    mesitas =Mesa.objects.all()
    return render(request, "AppReservas/mesas.html", {'mesitas':mesitas})

def busqueda_reserva(request):
    return render(request, "AppReservas/busquedaReserva.html")

def buscar(request):
    busqueda_reserva = request.GET.get("cliente", "")  # Obtén el valor del campo de entrada en lugar de "reservas"
    reservas = Reserva.objects.filter(cliente__nombre__icontains=busqueda_reserva)
    
    return render(request, "AppReservas/resultadosBusqueda.html", {"reservas": reservas, "busqueda_reserva": busqueda_reserva})
