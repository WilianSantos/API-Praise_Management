from rest_framework import viewsets, filters, generics

from django_filters.rest_framework import DjangoFilterBackend

from .models import Music, MusicChord, VersionMusic, Playlist, MusicCategory
from .serializers import MusicSerializers, MusicChordSerializers, VersionMusicSerializers, PlaylistSerializers,\
ListVersionMusicSerializer, MusicCategorySerializers


class MusicCategoryViewSet(viewsets.ModelViewSet):
    queryset = MusicCategory.objects.all()
    serializer_class = MusicCategorySerializers

    
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializers

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['title_music']
    search_fields = ['title_music', 'author', 'theme', 'category']


class MusicChordViewSet(viewsets.ModelViewSet):
    queryset = MusicChord.objects.all()
    serializer_class = MusicChordSerializers


class VersionMusicViewSet(viewsets.ModelViewSet):
    queryset = VersionMusic.objects.all()
    serializer_class = VersionMusicSerializers

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['author']
    search_fields = ['music', 'author']

class ListVersionMusic(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = VersionMusic.objects.filter(music_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListVersionMusicSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializers

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['date']
    search_fields = ['date', 'name']
