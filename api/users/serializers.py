from django.contrib.auth.models import User
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class GetTokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=128, required=True)
    password = serializers.CharField(max_length=128, required=True)


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=255, required=True, help_text='refresh token')


class RevokeTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, required=True)


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=255, required=True)
    expires_in = serializers.IntegerField(required=True)
    token_type = serializers.CharField(max_length=16, required=True)
    scope = serializers.CharField(max_length=1024, required=True)
    refresh_token = serializers.CharField(max_length=255, required=True)
