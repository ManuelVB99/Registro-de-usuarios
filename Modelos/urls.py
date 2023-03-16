from django.urls import path
from .views import *

urlpatterns = [
    path("registrodeclientes/", nuevos_clientes),
    path("clientes/", ver_clientes),
    path("borrarcliente/<cliente_id>", borrar_cliente),
    path("editarcliente/<cliente_id>", editar_cliente)

]