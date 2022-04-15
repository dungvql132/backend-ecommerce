from base64 import encode
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from api_basic.models import *
from api_basic.serializer import *
from django.contrib.auth import login
from api_basic.containt import *
import jwt

@api_view(['GET','POST'])
def loginAPIView(request):
  if request.method == "POST":
    try:
      data = JSONParser().parse(request)
      user = MyUser.objects.all().filter(email=data["email"],password=data["password"])
      serializer = UserSerializer(user,many=True)
      print("seriable:",len(serializer.data) == 1)
      token = None
      if len(serializer.data) == 1:
        token = jwt.encode(payload=data,key=SECRET_KEY,algorithm=ALGORITHM)
      else:
        raise Exception
      return Response(data={
        "data":data,
        "token":token,
        "message":MESSAGE_SUCCESS("login this page")
      }, status = status.HTTP_201_CREATED)
    except:
      return Response(data={
        "message":NOT_FOUND("the user")
      }, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def registerAPIView(request):
  if request.method == "POST":
    try:
      data = JSONParser().parse(request)
      user = MyUser.objects.all().filter(email=data["email"])
      serializerUser = UserSerializer(user,many=True)
      token = None
      if len(serializerUser.data) == 0:
        token = jwt.encode(payload=data,key=SECRET_KEY,algorithm=ALGORITHM)
      else:
        return Response(data={
        "message":ALREADY_EXIST("the user")
      }, status = status.HTTP_400_BAD_REQUEST)
      serializer = UserSerializer(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({
        "data": data,
        "token": token,
        "message":MESSAGE_SUCCESS("login this page")
      })
    except:
      return Response(data={
        "message":serializer.errors
      }, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def getCurrentUser(request):
  if request.method == "GET":
    try:
      token = request.META['HTTP_AUTHORIZATION']
      data = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
      return Response({
        "data": data,
        "token": token,
        "message":MESSAGE_SUCCESS("get current user")
      })
    except:
      return Response(data={
        "message":MESSAGE_ERROR
      }, status = status.HTTP_400_BAD_REQUEST)