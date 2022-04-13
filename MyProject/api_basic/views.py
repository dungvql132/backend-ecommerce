from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Article
from .serializer import ArticleSerializers


# Create your views here.
@api_view(['GET','POST'])
def article_list(request):
  if request.method == "GET":
    articles = Article.objects.all()
    serializer = ArticleSerializers(articles, many=True)
    return Response(data=serializer.data,status=status.HTTP_200_OK)
  elif request.method == "POST":
    data = JSONParser().parse(request)
    serializer = ArticleSerializers(data = data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data, status = status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
  try:
    article = Article.objects.get(pk = pk)
  except:
    return HttpResponse(status=404)

  if request.method == "GET":
    serializer = ArticleSerializers(article)
    return Response(data=serializer.data,status=status.HTTP_200_OK)
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