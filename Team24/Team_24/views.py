from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import login,hiringDetails,ProfileDashboard
from .serializers import MyModelSerializer,HiringSerializer,ProfileDashSerializer


class loginListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
    create_serializer = MyModelSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      todo_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = MyModelSerializer(todo_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)
  

  def get(self, request, id=None):
        if id:
          queryset = login.objects.filter(id=id)
      # Serialize todo item from Django queryset object to JSON formatted data
          read_serializer = MyModelSerializer(queryset)
        
          read_serializer = MyModelSerializer(queryset)

        else:
      # Get all todo items from the database using Django's model ORM
          queryset = login.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
        read_serializer = MyModelSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
  


class HiringListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
    create_serializer = HiringSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      todo_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = HiringSerializer(todo_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)
  

  def get(self, request, id=None):
        if id:
          queryset = hiringDetails.objects.filter(id=id)
      # Serialize todo item from Django queryset object to JSON formatted data
          read_serializer = HiringSerializer(queryset)
        
          read_serializer = HiringSerializer(queryset)

        else:
      # Get all todo items from the database using Django's model ORM
          queryset = hiringDetails.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
        read_serializer = HiringSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
  




class ProfileListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
    create_serializer = ProfileDashSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      todo_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = ProfileDashSerializer(todo_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)
  

  

  def get(self, request, id=None):
        if id:
          queryset = ProfileDashboard.objects.filter(id=id)
      # Serialize todo item from Django queryset object to JSON formatted data
          read_serializer = ProfileDashSerializer(queryset)
        
          read_serializer = ProfileDashSerializer(queryset)

        else:
      # Get all todo items from the database using Django's model ORM
          queryset = ProfileDashboard.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
        read_serializer = ProfileDashSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
  
  def update(self,instance,validated_data):
        current_funds = validated_data.get('funds')
        instance.funds+=current_funds
        instance.save()
        return instance

  
