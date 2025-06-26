from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    department=models.CharField(max_length=100 , default="")
    contract_years = models.IntegerField(default=0)
    shift = models.CharField(max_length=100 , default="Morning")
    experience =models.IntegerField(default=0)
    performance = models.FloatField()
    
    email=models.EmailField(default="123456@company.com")

def __str__(self):
    return self.name