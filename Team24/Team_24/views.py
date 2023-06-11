from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import login,hiringDetails,ProfileDashboard,internRegister
from .serializers import MyModelSerializer,HiringSerializer,ProfileDashSerializer,RegisterSerializer


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
          queryset = hiringDetails.objects.get(id=id)
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
  
  def put(self, request, id=None):
        try:
      # Check if the todo item the user wants to update exists
          todo_item = ProfileDashboard.objects.filter(id=id)
        except ProfileDashboard.DoesNotExist:
      # If the todo item does not exist, return an error response
         return Response({'errors': 'This todo item does not exist.'}, status=400)

    # If the todo item does exists, use the serializer to validate the updated data
        update_serializer = ProfileDashSerializer(todo_item, data=request.data)

    # If the data to update the todo item is valid, proceed to saving data to the database
        if update_serializer.is_valid():

      # Data was valid, update the todo item in the database
          todo_item_object = update_serializer.save()

      # Serialize the todo item from Python object to JSON format
          read_serializer = ProfileDashSerializer(todo_item_object)

      # Return a HTTP response with the newly updated todo item
          return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
        return Response(update_serializer.errors, status=400)

  




class RegisterListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def post(self, request):
        # Pass JSON data from user POST request to serializer for validation
    create_serializer = RegisterSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new todo item record in the database
      todo_item_object = create_serializer.save()

      # Serialize the new todo item from a Python object to JSON format
      read_serializer = RegisterSerializer(todo_item_object)

      # Return a HTTP response with the newly created todo item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)
  

  

  def get(self, request, id=None):
        if id:
          queryset = internRegister.objects.filter(id=id)
      # Serialize todo item from Django queryset object to JSON formatted data
          read_serializer = RegisterSerializer(queryset)
        
          read_serializer = RegisterSerializer(queryset)

        else:
      # Get all todo items from the database using Django's model ORM
          queryset = internRegister.objects.all()

      # Serialize list of todos item from Django queryset object to JSON formatted data
        read_serializer = RegisterSerializer(queryset, many=True)

    # Return a HTTP response object with the list of todo items as JSON
        return Response(read_serializer.data)
  
 