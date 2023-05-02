from django.db import models
from rest_framework import serializers
from django.http import HttpResponse
# Models

class ProductsModel_Foroosh(models.Model):
     name = models.CharField(max_length=225,unique=True)
     price = models.IntegerField(help_text="enter the item's price")
     number = models.IntegerField(help_text='enter the number of goods')
     add_date=models.DateTimeField(auto_now_add=True)
     expire_date=models.DateTimeField(help_text="enter the item's price")

     def __str__(self):
          return self.name


class ProductSerializers(serializers.ModelSerializer):
     
     class Meta:
          model = ProductsModel_Foroosh
          fields = ['name', 'price', "number", 'add_date', 'expire_date']
          depth=1
     # def to_representation(self, instance):
     #      data=super().to_representation(instance)
     #      data['tese']=6748765
     #      return data

def site_Foroosh_view_model(request):
     return HttpResponse('the selling products list :')