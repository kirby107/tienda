from django.urls import path
from .views import crear_pedido, listar_pedidos

urlpatterns = [
    path('', listar_pedidos, name='listar_pedidos'),
    path('crear/', crear_pedido, name='crear_pedido'),
]