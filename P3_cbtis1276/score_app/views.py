from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def con(request):
    return render(request,"contactos.html")

def emp(request):
    return render(request,"empleados.html")

def suc(request):
    return render(request,'sucursal.html')

def cli(request):
    return render(request,'clientes.html')

def pro(request):
    return render(request,'provedor.html')
# Create your views here.
