from rest_framework import viewsets, filters, generics

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ChurchSerializer, CultSerializer, ListCultChurchSerializer, FunctionSerializers,\
    MemberSerializers
from .models import Church, Cult, Function, Member


class ChurchViewSet(viewsets.ModelViewSet):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    

class CultViewSet(viewsets.ModelViewSet):
    queryset = Cult.objects.all()
    serializer_class = CultSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['theme', 'date']


class ListCultChurch(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Cult.objects.filter(church_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListCultChurchSerializer


class FunctionViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializers

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name']


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializers

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'function']
