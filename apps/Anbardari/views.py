from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import *
from django.db.models import Sum
##for anbardar to be able to add - delete products
class ProductView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        queryset = ProductsModel.objects.all()
        serializers = ProductSerializers(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


    def post(self, request):
        data = request.data
        Name = data['name']
        Price = data['price']
        Number = data['number']
        Expire_date = data['expire_date']
        Product = ProductsModel(name=Name, price=Price, number=Number, expire_date=Expire_date)
        Product.save()
        return Response(status=status.HTTP_200_OK)


    def delete(self, request):
        data = request.data
        product = ProductsModel.objects.get(name=data['name'])
        product.delete()
        return Response(status=status.HTTP_200_OK)


       
    def put(self, request):
        data = request.data
        product = ProductsModel.objects.get(pk=data['id'])
        product.name = data['name']
        product.price = data['price']
        product.number = data['number']
        product.add_date = data['AddDate']

##for showing the Total in admin dashboard
def Items_total_sell_price():
    print(models.sell_price_total)

