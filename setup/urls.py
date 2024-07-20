from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.church.views import ChurchViewSet, CultViewSet, ListCultChurch
from apps.music.views import MusicViewSet, MusicChordViewSet, VersionMusicViewSet, PlaylistViewSet,\
ListVersionMusic

router = routers.DefaultRouter()

router.register('church', ChurchViewSet, basename='Igreja')
router.register('cult', CultViewSet, basename='Culto')

router.register('music', MusicViewSet, basename='Musica')
router.register('music-chord', MusicChordViewSet, basename='Acorde')
router.register('version-music', VersionMusicViewSet, basename='Versoes')
router.register('playlist', PlaylistViewSet, basename='Playlist')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('cult/<int:pk>/church/', ListCultChurch.as_view()),
    path('version-music/<int:pk>/music/', ListVersionMusic.as_view()),
]
