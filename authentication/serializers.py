from rest_framework import serializers

from user.serializers import UserSerializer


class AuthOutputSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
    user = UserSerializer()


class AuthInputSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class AuthRefreshInputSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(required=True)


class AuthRefreshOutputSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True)
