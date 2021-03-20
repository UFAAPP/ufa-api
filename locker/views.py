from rest_framework import viewsets

from locker.models import Locker
from locker.serializers import LockerSerializer


class LockerView(viewsets.ModelViewSet):
    queryset = Locker.objects.all()
    serializer_class = LockerSerializer
