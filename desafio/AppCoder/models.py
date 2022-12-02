from django.db import models

# Create your models here.
class Familiar(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    date_birth = models.DateField()
    children = models.BooleanField()
    
    def __str__(self):
        return self.name+ " " + self.lastname
