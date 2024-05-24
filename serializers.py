
from rest_framework import serializers
from .models import ModelData

class ModelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelData
        fields = '__all__'
