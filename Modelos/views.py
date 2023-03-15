from django.shortcuts import render
from .models import *

#Con esta función vamos a registrar nuevos clientes.
def nuevos_clientes (request):
    if request.method == 'POST':
        nuevo_cliente = clientes(mail = request.post("mail"), nombre = request.post("nombre"),apellido = request.post("apellido"),fecha_registro = request.post("fecha_registro"))
        nuevo_cliente.save()
        return render(request, "clientes.html")
    return render(request, "clientes.html")
def ver_clientes(request):
    clientes = clientes.object.all()
    pass


