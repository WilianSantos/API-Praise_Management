from rest_framework import viewsets

from .models import Cast
from .serializers import CastSerializers


class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializers
