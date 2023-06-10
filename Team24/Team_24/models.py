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
    

class hiringDetails(models.Model):
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

    






