from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api_basic.models import *
from api_basic.serializer import *

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
def laptop_listAPIView(request):
  if request.method == "GET":
    lstLaptop = LaptopSerializer(Laptop.objects.all(), many=True).data
    for laptop in lstLaptop:
      laptop["product"]= getProduct(laptop["product"])
    return Response(data=lstLaptop,status=status.HTTP_200_OK)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    serializerProduct = ProductSerializer(data=data)
    if serializerProduct.is_valid():
      serializerProduct.save()
    
    print("serializerProduct: ",serializerProduct.data)
    return Response(data=serializerProduct.data, status = status.HTTP_201_CREATED)
    # return Response(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
  try:
    article = Article.objects.get(pk = pk)
  except:
    pass

  if request.method == "GET":
    serializer = ArticleSerializers(article)
    return Response(status=status.HTTP_200_OK,data=serializer.data)
  elif request.method == "PUT":
    data = JSONParser().parse(request)
    serializer = ArticleSerializers(article,data = data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data, status = status.HTTP_202_ACCEPTED)
    return Response(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    article.delete()
    return HttpResponse(status = 204)