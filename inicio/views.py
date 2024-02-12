from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from inicio.models import Cliente
import random
def inicio(request): 
    #   archivo_abierto = open (r"C:\Users\facul\Desktop\López_Renaud_Facundo-PreEntrega#3\templates\inicio.html","r" )
  #  template = Template(archivo_abierto.read())
  #  archivo_abierto.close()
    
    #contexto = Context()
   # template_renderizado = template.render(contexto)
   # clientes = Cliente.objects.all()
   # return HttpResponse(template_renderizado)
    clientes = Cliente.objects.all()
    return render(request, "inicio.html", {})

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {"clientes": clientes})

def crear_cliente(request, nombre,apellido, edad):
    cliente = Cliente (nombre=nombre, apellido=apellido, edad=edad, dinero_gastado=random.randint(1,100))
    cliente.save() 
    return render(request, "crear_cliente.html", {"cliente":cliente})


