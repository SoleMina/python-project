from django.shortcuts import render
from .models import *
from django.http import HttpResponse
#from django.template import Template, loader
from AppCoder.forms import ProductoForm, EmpresaForm, MarcaForm


# Create your views here.
def inicio(request):
    return render (request, "AppCoder/inicio.html")

def marca(request):
    #return HttpResponse("Página de cursos")
    return render (request, "AppCoder/marca.html")

def producto(request):
    #return HttpResponse("Página de producto")
    if request.method=="POST":
        form=ProductoForm(request.POST)
        print("-------------------")
        print(form)
        print("-------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            name=informacion["name"]
            description=informacion["description"]
            stock=informacion["stock"]
            price=informacion["price"]
            company=informacion["company"]
            
            producto1=Producto(name=name, description=description, stock=stock, price=price, company=company)
            producto1.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Producto creado exitosamente"})
    else:
        formulario=ProductoForm()
    return render(request, "AppCoder/producto.html", {"form": formulario})

def empresa(request):
    #return HttpResponse("Página de producto")
    if request.method=="POST":
        form=EmpresaForm(request.POST)
        print("-------------------")
        print(form)
        print("-------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            name=informacion["name"]
            address=informacion["address"]
            year_creation=informacion["year_creation"]
            
            empresa1=Empresa(name=name, address=address, year_creation=year_creation)
            empresa1.save()
            return render (request, "AppCoder/inicio.html", {"mensaje": "Empresa creado exitosamente"})
    else:
        formulario=EmpresaForm()
    return render(request, "AppCoder/empresa.html", {"form": formulario})


def empresaFormulario(request):
    formulario = ''
    if request.method == "POST":
        form=EmpresaForm(request.POST)
        print("-------------------")
        print(form)
        print("-------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            name=informacion["name"]
            address=informacion["address"]
            year_creation=informacion["year_creation"]
    
            empresa1 = Empresa(name=name, address=address, year_creation=year_creation)
            empresa1.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario=EmpresaForm()
    return render(request, "AppCoder/empresaFormulario.html", {"form": formulario})

def marcaFormulario(request):
    formulario = ''
    if request.method == "POST":
        form=MarcaForm(request.POST)
        print("-------------------")
        print(form)
        print("-------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            name=informacion["name"]
            description=informacion["description"]
    
            marca1 = Marca(name=name, description=description)
            marca1.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario=MarcaForm()
    return render(request, "AppCoder/marcaFormulario.html", {"form": formulario})

def productoFormulario(request):
    formulario = ''
 
    if request.method == "POST":
        form=ProductoForm(request.POST)
        print("-------------------")
        print(form)
        print("-------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            name=informacion["name"]
            description=informacion["description"]
            stock=informacion["stock"]
            price=informacion["price"]
            company=informacion["company"]

            producto1 = Producto(name=name, description=description, stock=stock, price=price, company=company)
            producto1.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario=ProductoForm()
    return render(request, "AppCoder/productoFormulario.html", {"form": formulario})

def busquedaProducto(request):
    return render(request, "AppCoder/busquedaProducto.html")

def busquedaEmpresa(request):
    return render(request, "AppCoder/busquedaEmpresa.html")

def buscar(request):
    if request.GET["name"]:
        name=request.GET["name"]
        productos=Producto.objects.filter(name=name)
        return render(request, 'AppCoder/resultadosBusqueda.html', {"productos": productos})
    else:
        return render(request, 'AppCoder/busquedaProducto.html', {"mensaje": "Che, ingresá un producto"})
