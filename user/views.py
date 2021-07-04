from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import UserSerializer, \
    UserInputSerializer
from user.services import UserService


class UsersView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        pass

    def post(self, request):
        serializer = UserInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = UserService()
        response = service.create_user(**serializer.validated_data)

        return Response(data=UserSerializer(response).data, status=status.HTTP_201_CREATED)
