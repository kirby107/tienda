from django.shortcuts import redirect
from .models import Carrito
from productos.models import Producto

def agregar_carrito(request, producto_id):
    if not request.user.is_authenticated:
        return redirect('registro')

    producto = Producto.objects.get(id=producto_id)
    Carrito.objects.create(usuario=request.user, producto=producto)
    return redirect('lista_productos')