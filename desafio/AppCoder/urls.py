from django.urls import path
from AppCoder.views import *

urlpatterns = [
 path('producto/', producto, name='producto'),
 path('empresa/', empresa, name='empresa'),
 path('marca/', marca, name='marca'),
 path('productoFormulario', productoFormulario, name='productoFormulario'),
 path('empresaFormulario', empresaFormulario, name='empresaFormulario'),
 path('marcaFormulario', marcaFormulario, name='marcaFormulario'),
 path('busquedaProducto', busquedaProducto, name='busquedaProducto'),
 path('busquedaEmpresa', busquedaEmpresa, name='busquedaEmpresa'),
 path('buscar/', buscar, name='buscar'),
 path('', inicio, name='inicio'),   
]