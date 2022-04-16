from base64 import encode
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api_basic.models import *
from api_basic.serializer import *
from api_basic.containt import *

def getAddress(pk):
  address = AddressSerializer(Address.objects.get(pk=pk)).data
  return address

def getSupplier(pk):
  supplier = SupplierSerializer(Supplier.objects.get(pk=pk)).data
  supplier["address"]=getAddress(supplier["address"])
  return supplier

def getProduct(pk):
  product = ProductSerializer(Product.objects.get(pk=pk)).data
  product["medias"] = []
  lstproductmedia = ProductMediaSerializer(ProductMedia.objects.all(),many=True).data
  for productmedia in lstproductmedia:
    if productmedia['product']==pk:
      product["medias"].append(MediaSerializer(Media.objects.get(pk=productmedia['media'])).data["link"])
  product["supplier"] = getSupplier(product["supplier"])
  return product


@api_view(['GET','POST'])
def product_listAPIView(request):
  if request.method == "GET":
    # try:
      lstLaptop = LaptopSerializer(Laptop.objects.all(), many=True).data
      for laptop in lstLaptop:
        laptop["product"]= getProduct(laptop["product"])
      lstClothes = ClothesSerializer(Clothes.objects.all(), many=True).data
      for clothes in lstClothes:
        clothes["product"]= getProduct(clothes["product"])
      lstResult = []
      lstResult.append(lstLaptop)
      lstResult.append(lstClothes)
      return Response(data={
        "data":lstResult,
        "message":MESSAGE_SUCCESS("get all product")
      }, status = status.HTTP_201_CREATED)
    # except:
    #   return Response(data={
    #     "message":MESSAGE_ERROR
    #   }, status = status.HTTP_400_BAD_REQUEST)