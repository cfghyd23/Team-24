from django.db import models
from rest_framework import serializers


# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    class Meta:
        app_label = "Team_24"

    def __str__(self):
        return self.username
    
class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'

choices = ()

class internRegister(models.Model):
     fullname = models.CharField(max_length=20)
     email = models.EmailField(max_length=20)
     gender = 




