from django.db import models


class Products(models.Model):
     name = models.CharField(max_length=225)
     price = models.FloatField()
     number = models.IntegerField()
     add_date=models.DateTimeField(auto_now_add=True)
     expire_date=models.DateTimeField()

     def __str__(self):
          return self.name

class Gozaresh(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)



