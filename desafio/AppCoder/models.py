from django.db import models

# Create your models here.
class Empresa(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    year_creation = models.IntegerField()
    
    def __str__(self):
        return self.name+ " " + self.address

class Producto(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    stock = models.IntegerField()
    price = models.IntegerField()
    company = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name+ " " + self.description

class Marca(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name+ " " + self.description
    