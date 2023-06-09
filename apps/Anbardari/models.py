from django.db import models
from rest_framework import serializers

# Models

class ProductsModel(models.Model):
     name = models.CharField(max_length=225,unique=True)
     price = models.IntegerField(help_text="enter the item's price")
     number = models.IntegerField(help_text='enter the number of goods')
     add_date=models.DateTimeField(auto_now_add=True)
     expire_date=models.DateTimeField(help_text="enter the item's price")

     def __str__(self):
          return self.name

class GozareshModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    def __str__(self):
          return self.product.name

# Serializers

class ProductSerializers(serializers.ModelSerializer):
     
     class Meta:
          model = ProductsModel
          fields = ['name', 'price', "number", 'add_date', 'expire_date']
          depth=1
     # def to_representation(self, instance):
     #      data=super().to_representation(instance)
     #      data['tese']=6748765
     #      return data

class GozareshSerializers(serializers.ModelSerializer):
     class Meta:
          model = GozareshModel
          fields = ['product']
          depth = 1
 
# class sell_price_total(models.model.FloatField()):
#      sell_price_total=ProductsModel.price * ProductsModel.number

     


