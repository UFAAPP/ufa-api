from rest_framework import viewsets

from lawsuit.models import Lawsuit
from lawsuit.serializers import LawsuitPostSerializer, LawsuitGetSerializer


class LawsuitView(viewsets.ModelViewSet):
    queryset = Lawsuit.objects.all()
    serializer_class = LawsuitGetSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST' or method == 'PATCH':
            return LawsuitPostSerializer
        else:
            return LawsuitGetSerializer



