from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json

@api_view(['GET']) #1° GET
def get_users(request):

    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET']) #2° GET
def get_by_nick(request, nick):
    
    try:
        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
@api_view(['GET']) #3° GET
def get_by_nick_with_param(request):

    if request.method == 'GET':
        try:
            if request.GET['user']:
                user_nickname = request.GET['user']

                try:
                    user = User.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                serializer = UserSerializer(user)
                return Response(serializer.data)
            
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def create_user(request):
    
    if request.method == 'POST':
        new_user = request.data
        serializer = UserSerializer(data=new_user)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT']) #1° PUT
def edit_user(request):

    if request.method == 'PUT':

        nickname = request.data['user_nickname']

        try:
            updated_user = User.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT']) #2° PUT
def edit_user2(request, nick):
        
    if request.method == 'PUT':
        try:
            user = User.objects.get(pk=nick)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) #1° DELETE
def delete_user(request):
        
    if request.method == 'DELETE':
        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user_to_delete.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE']) #2° DELETE
def delete_user2(request, nick):

    if request.method == 'DELETE':
        try:
            user_to_delete = User.objects.get(pk=nick)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_to_delete.delete()    
        return Response(status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)
   