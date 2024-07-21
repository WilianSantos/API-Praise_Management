from django.contrib import admin
from django.urls import path, include

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.church.views import ChurchViewSet, CultViewSet, ListCultChurch, FunctionViewSet, MemberViewSet
from apps.music.views import MusicViewSet, MusicChordViewSet, VersionMusicViewSet, PlaylistViewSet,\
ListVersionMusic
from apps.praise.views import CastViewSet

router = routers.DefaultRouter()

# Rotas de Church
router.register('church', ChurchViewSet, basename='Igreja')
router.register('cult', CultViewSet, basename='Culto')
router.register('fuction', FunctionViewSet, basename='Funcao')
router.register('member', MemberViewSet, basename='Membro')

# Rotas de Music
router.register('music', MusicViewSet, basename='Musica')
router.register('music-chord', MusicChordViewSet, basename='Acorde')
router.register('version-music', VersionMusicViewSet, basename='Versoes')
router.register('playlist', PlaylistViewSet, basename='Playlist')

# Rotas de Praise
router.register('cast', CastViewSet, basename='Escalacao')

# Documentação
schema_view = get_schema_view(
   openapi.Info(
      title="API de Gerenciamento do louvor",
      default_version='v1',
      description="Organizador das musicas e gerenciamento de escalações do louvor da igreja",
      terms_of_service="#",
      contact=openapi.Contact(email="wilian.santos.dev@alura.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('gerenciamento-louvor-admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('cult/<int:pk>/church/', ListCultChurch.as_view()),
    path('version-music/<int:pk>/music/', ListVersionMusic.as_view()),
]
