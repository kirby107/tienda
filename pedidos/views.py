from django.shortcuts import redirect
from .models import Pedido, DetallePedido
from carrito.models import Carrito

def crear_pedido(request):
    if not request.user.is_authenticated:
        return redirect('registro')

    carrito = Carrito.objects.filter(usuario=request.user)
    pedido = Pedido.objects.create(usuario=request.user)

    for item in carrito:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad
        )

    carrito.delete()
    return redirect('lista_productos')