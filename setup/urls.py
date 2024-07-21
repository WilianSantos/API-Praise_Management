from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.church.views import ChurchViewSet, CultViewSet, ListCultChurch, FunctionViewSet, MemberViewSet
from apps.music.views import MusicViewSet, MusicChordViewSet, VersionMusicViewSet, PlaylistViewSet,\
ListVersionMusic
from apps.praise.views import CastViewSet

router = routers.DefaultRouter()

router.register('church', ChurchViewSet, basename='Igreja')
router.register('cult', CultViewSet, basename='Culto')
router.register('fuction', FunctionViewSet, basename='Funcao')
router.register('member', MemberViewSet, basename='Membro')

router.register('music', MusicViewSet, basename='Musica')
router.register('music-chord', MusicChordViewSet, basename='Acorde')
router.register('version-music', VersionMusicViewSet, basename='Versoes')
router.register('playlist', PlaylistViewSet, basename='Playlist')

router.register('cast', CastViewSet, basename='Escalacao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('cult/<int:pk>/church/', ListCultChurch.as_view()),
    path('version-music/<int:pk>/music/', ListVersionMusic.as_view()),
]
