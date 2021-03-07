import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, viewsets, permissions
from rest_framework.views import APIView

from company.views import CompanySerializer
from user.models import User
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import exceptions
from util.auth import generate_access_token, generate_refresh_token
from rest_framework.permissions import AllowAny


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserCompanySerializer(serializers.ModelSerializer):

    company = CompanySerializer()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'is_active', 'social_number', 'company']
        extra_kwargs = {
            'password': {'write_only': True}
        }


class UsersView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post', 'patch']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'username']


class LoginRefreshSerializer(serializers.Serializer):

    refresh_token = serializers.CharField(required=True)


class UsersAuthView(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(request_body=LoginSerializer, responses={200: UserCompanySerializer(many=False)})
    def post(self, request):
        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')
        response = Response()
        if (username is None) or (password is None):
            raise exceptions.AuthenticationFailed(
                'username and password required')

        user = User.objects.filter(social_number=username) | User.objects.filter(email=username)
        user = user.first()
        if user is None:
            raise exceptions.AuthenticationFailed('user not found or wrong password')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('user not found or wrong password')

        serialized_user = UserCompanySerializer(user).data

        access_token = generate_access_token(user)
        refresh_token = generate_refresh_token(user)

        response.data = {
            'access_token': access_token,
            'user': serialized_user,
            'refresh_token': refresh_token
        }

        return response

    @swagger_auto_schema(request_body=LoginRefreshSerializer, responses={200: LoginRefreshSerializer(many=False)})
    def put(self, request):
        '''
        To obtain a new access_token this view expects a valid refresh_token
        '''
        User = get_user_model()
        refresh_token = request.data.get('refresh_token')
        if refresh_token is None:
            raise exceptions.AuthenticationFailed(
                'Authentication credentials were not provided.')
        try:
            payload = jwt.decode(
                refresh_token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                'expired refresh token, please login again.')

        user = User.objects.filter(id=payload.get('user_id')).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')

        access_token = generate_access_token(user)
        return Response({'access_token': access_token})

