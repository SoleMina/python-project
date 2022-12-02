from django.shortcuts import render
from .models import Familiar
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.
def familiar(request):
    familiar1=Familiar(name="Sam", lastname="Prado", age= 22, date_birth="2000-12-02", children=False)
    familiar1.save()
    familiar2=Familiar(name="Carlos", lastname="Gutierrez", age= 29, date_birth="1999-10-01", children=True)
    familiar2.save()
    familiar3=Familiar(name="Ana", lastname="Cuellar", age= 19, date_birth="1998-01-01", children=False)
    familiar3.save()
    
    diccionario={"familiares": [familiar1, familiar2, familiar3] }
    
    template = loader.get_template('template.html')
    
    documento = template.render(diccionario)
    return HttpResponse(documento)
    
    # cadena_Texto=f"Familiar guardado: {familiar1.name} {familiar1.lastname} tiene {str(familiar1.age)} años, nació {familiar1.date_birth}  y tiene  {familiar1.children} hijos"
    # return HttpResponse(cadena_Texto)