from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


# Create your models here.

class login(models.Model):
    id = models.AutoField(
    primary_key=True
  )
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=1200)

    def save(self,*args,**kwargs):
         self.password = make_password(self.password)
         super(login,self).save(*args,**kwargs)
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
     
     def save(self,*args,**kwargs):
         self.password = make_password(self.password)
         super(internRegister,self).save(*args,**kwargs)



class ProfileDashboard(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    funds = models.IntegerField()


    

class hiringDetails(models.Model):
    id = models.AutoField(
    primary_key=True
  )
    email = models.EmailField(max_length=20)
    fullname = models.CharField(max_length=20)
    options1 = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others'),
        (4, 'Prefer not to say'),
    )
    gender = models.IntegerField(choices=options1)
    dob = models.DateField()
    phonenumber = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)  
    education = models.CharField(max_length=20)
    options2 = (
        (1, 'In-Person'),
        (2, 'Virtual'),
    )
    internshiprole = models.IntegerField(choices=options2)
    tellusaboutyourself = models.CharField(max_length=20)



    






