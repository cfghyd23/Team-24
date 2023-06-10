from rest_framework import serializers
from .models import login


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = login
        fields = '__all__'