from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User


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



class internRegister(models.Model):
     firstname = models.CharField(max_length=20)
     lastname = models.EmailField(max_length=20)
     email = models.EmailField(max_length=30)
     password = models.CharField(max_length=20)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    admin_remark = models.CharField(max_length=500,default="")
    profile_image = models.ImageField(upload_to="profile_image/",blank=True)


    def __str__(self):
	    return self.user.username

    






