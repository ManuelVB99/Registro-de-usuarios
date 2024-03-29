"""RegistroDeClientes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", inicio),
    path("", include("Modelos.urls")),
    path("login/", login_request),
    path("registro/", registro),
    path('logout/', LogoutView.as_view(template_name='inicio.html'), name="Logout"),
    path("perfil/", perfilView),
    path("editarperfil/", editarperfil),
    path("cambiarcontraseña/", cambiarpassword)


]
