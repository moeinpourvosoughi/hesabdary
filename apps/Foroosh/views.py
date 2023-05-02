from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import *
from django.http import HttpResponse

class site_Foroosh_part(APIView):
    def get(self, request):
        queryset = ProductsModel_Foroosh.objects.all()
        serializers = ProductSerializers(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
class ProductSellReport(models.Model):
    name=models.CharField(max_length=225,unique=True)
    price=models.IntegerField()
    number=models.IntegerField(max_length=10000)    