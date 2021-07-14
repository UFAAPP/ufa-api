# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from user.services import AddUser
# from gym_schedule.permissions import IsAuthenticatedOrCreateOnly
from user.serializers import UserSerializer

from util.mixins import ApiErrorsMixin


class UserCreateApi(ApiErrorsMixin, APIView):

    def __init__(self):
        self.add_user = AddUser()

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        self.add_user.add(**user_serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

