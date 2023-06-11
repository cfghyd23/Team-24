from rest_framework import serializers
from .models import login,hiringDetails,ProfileDashboard,internRegister


class MyModelSerializer(serializers.ModelSerializer):
      username = serializers.CharField(max_length=1000, required=True)
      password = serializers.CharField(max_length=1000, required=True)
      def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return login.objects.create(
        username=validated_data.get('username'), password=validated_data.get('password')
        
    )

      def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.username= validated_data.get('username', instance.username)
        instance.password= validated_data.get('password', instance.password)
        instance.save()
        return instance

      class Meta:
        model = login
        fields = '__all__'


class HiringSerializer(serializers.ModelSerializer):
      email = serializers.CharField(max_length=1000, required=True)
      fullname = serializers.CharField(max_length=1000, required=True)
      gender = serializers.CharField(max_length=10, required=True)
      phonenumber = serializers.CharField(max_length=20, required=True)
      dob = serializers.DateField(required=True)


      def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return hiringDetails.objects.create(
        email=validated_data.get('email'), fullname=validated_data.get('fullname'),gender=validated_data.get('gender'),
        phonenumber=validated_data.get('phonenumber'),dob=validated_data.get('dob'),
        state=validated_data.get('state'),
        city=validated_data.get('city'),
        education=validated_data.get('education'),
        internshiprole=validated_data.get('internshiprole'),
        tellusaboutyourself=validated_data.get('tellusaboutyourself')
        
    )

      def update(self, instance, validated_data):
     # Once the request data has been validated, we can update the todo item instance in the database
        instance.email= validated_data.get('email', instance.email)
        instance.fullname= validated_data.get('fullname', instance.fullname)
        instance.gender= validated_data.get('gender', instance.gender)
        instance.phonenumber= validated_data.get('phone', instance.phonenumber)
        instance.dob= validated_data.get('dob', instance.dob)
        instance.state= validated_data.get('dob', instance.state)
        instance.city= validated_data.get('dob', instance.city)
        instance.education= validated_data.get('dob', instance.education)
        instance.internshiprole= validated_data.get('dob', instance.internshiprole)
        instance.tellusaboutyourself= validated_data.get('dob', instance.tellusaboutyourself)

        instance.save()
        return instance

      class Meta:
        model = hiringDetails
        fields = '__all__'
 


    


class ProfileDashSerializer(serializers.ModelSerializer):
      email = serializers.CharField(max_length=1000, required=True)
      fullname = serializers.CharField(max_length=1000, required=True)
      funds = serializers.IntegerField(required=True)


      def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return ProfileDashboard.objects.create(
        email=validated_data.get('email'), 
        fullname=validated_data.get('fullname'),
        funds = validated_data.get('funds')
        
    )

      def update(self, instance, validated_data):
         # Once the request data has been validated, we can update the todo item instance in the database
        #instance.email= validated_data.get('email', instance.email)
        #instance.fullname= validated_data.get('fullname', instance.fullname)
        instance.funds += validated_data.get('funds')    

        instance.save()
        return instance

      class Meta:
        model = ProfileDashboard
        fields = '__all__'
 


class RegisterSerializer(serializers.ModelSerializer):
      firstname = serializers.CharField(max_length=1000, required=True)
      lastname = serializers.CharField(max_length=1000, required=True)
      email= serializers.EmailField(max_length=30,required=True)
      password = serializers.CharField(max_length=1000, required=True)


      def create(self, validated_data):
    # Once the request data has been validated, we can create a todo item instance in the database
        return internRegister.objects.create(
        firstname=validated_data.get('firstname'), 
        lastname=validated_data.get('lastname'),
        email = validated_data.get('email'),
        password=validated_data.get('password')
        
    )


      class Meta:
        model = internRegister
        fields = '__all__'
 