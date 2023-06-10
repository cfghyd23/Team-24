from django.shortcuts import render
from .models import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from .serializers import MyModelSerializer



class MyModelView(APIView):
    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the validated data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.




