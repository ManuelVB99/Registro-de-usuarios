from django.urls import path
from .views import *

urlpatterns = [
    path("registrodeclientes/", nuevos_clientes),

]