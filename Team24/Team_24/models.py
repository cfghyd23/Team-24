from django.db import models
from rest_framework import serializers

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    

    def __str__(self):
        return self.username
    
class MyModelserializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'


