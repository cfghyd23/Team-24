from rest_framework import serializers
from .models import login


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

    