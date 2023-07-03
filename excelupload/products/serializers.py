from rest_framework import serializers
from .models import Productmodel,Calendarmodel

class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productmodel
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendarmodel
        fields = '__all__'