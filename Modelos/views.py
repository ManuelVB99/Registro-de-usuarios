from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

#Con esta función vamos a registrar nuevos clientes.
def nuevos_clientes(request):
    try:
        if request.method == 'POST':
            nuevo_cliente = Clientes(mail=request.POST["mail"], nombre=request.POST["nombre"], apellido=request.POST["apellido"], fecha_registro=request.POST["fecha_registro"])
            nuevo_cliente.save()
            return render(request, "clientes.html")
    except:
        return render(request, "clientes.html")
    return render(request, "clientes.html")


#Con esta función vamos a poder ver todos los clientes de la base de datos.
@login_required
def ver_clientes(request):
    clientes = Clientes.objects.all()
    return render(request, "verclientes.html", {"clientes": clientes})

#Con esta función vamos a poder ver eliminar clientes de la base de datos.
@login_required
def borrar_cliente(request, cliente_id):
    clientes = Clientes.objects.get(id = cliente_id)
    clientes.delete()

    clientes = Clientes.objects.all()
    return render(request, "verclientes.html", {"clientes": clientes})

#Con esta función vamos a poder ver editar clientes de la base de datos.
@login_required
def editar_cliente(request, cliente_id):
    cliente = Clientes.objects.get(id=cliente_id)

    if request.method == 'POST':
        formulario = EditarClientes(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente.mail = info["mail"]
            cliente.nombre = info["nombre"]
            cliente.apellido = info["apellido"]
            cliente.fecha_registro = info["fecha_registro"]
            cliente.save()
            cliente = Clientes.objects.all()
            return render(request, "verclientes.html", {"clientes":cliente})
    else:
        formulario = EditarClientes(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'mail': cliente.mail, "fecha_registro": cliente.fecha_registro})
    return render(request, "editarcliente.html", {"formulario": formulario})





