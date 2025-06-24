from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    age = models.IntegerField()
    contract_years = models.IntegerField()
    shift = models.CharField(max_length=100)
    performance = models.FloatField()

def __str__(self):
    return self.name