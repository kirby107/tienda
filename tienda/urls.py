"""
URL configuration for tienda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from productos.views import lista_productos
from carrito.views import agregar_carrito
from pedidos.views import crear_pedido
from usuarios.views import registro

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lista_productos, name='lista_productos'),
    path('registro/', registro, name='registro'),

    path('carrito/agregar/<int:producto_id>/', agregar_carrito),
    path('pedido/', crear_pedido),
]