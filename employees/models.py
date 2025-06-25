from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    department=models.CharField(max_length=100)
    contract_years = models.IntegerField()
    shift = models.CharField(max_length=100)
    experience =models.IntegerField()
    performance = models.FloatField()
    
    email=models.EmailField(default="123456@company.com")

def __str__(self):
    return self.name