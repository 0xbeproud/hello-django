from rest_framework import serializers

from api.models import Demo


class CreateDemoRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'


class DemoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = '__all__'
