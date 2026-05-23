from django.shortcuts import render
from .models import Producto
from .models import Categoria

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista.html', {'productos': productos})

def tienda(request):
    categoria_id = request.GET.get('categoria')

    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)

    return render(request, "productos/tienda.html", {
        "productos": productos,
        "categorias": categorias
    })