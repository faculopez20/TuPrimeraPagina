from django.urls import path
from inicio.views import inicio, crear_cliente, clientes

urlpatterns = [
    path('', inicio, name="inicio"),
    #path("cliente/<str:nombre>/<str:apellido>/<int:edad>/", crear_cliente, name="crear_cliente"),
    path("cliente/", clientes, name= clientes),
    path("cliente/nuevo/", crear_cliente, name="crear_cliente"),
    ]
