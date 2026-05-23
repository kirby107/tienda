from django.shortcuts import render

def listar_pedidos(request):
    return render(request, 'pedidos.html')

def crear_pedido(request):
    return render(request, 'crear_pedido.html')