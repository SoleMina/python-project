from django import forms

class ProductoForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    stock = forms.IntegerField()
    price = forms.IntegerField()
    company = forms.CharField(max_length=50)

class EmpresaForm(forms.Form):
    name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=50)
    year_creation = forms.IntegerField()

class MarcaForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
