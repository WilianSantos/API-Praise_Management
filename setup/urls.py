from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.church.views import ChurchViewSet, CultViewSet, ListCultChurch, FunctionViewSet, MemberViewSet
from apps.music.views import MusicViewSet, MusicChordViewSet, VersionMusicViewSet, PlaylistViewSet,\
ListVersionMusic
from apps.praise.views import CastViewSet
from apps.user.views import UserViewSet, RegisterAPI, LoginView
from knox import views as knox_views

router = routers.DefaultRouter()

# Rotas de Church
router.register('church', ChurchViewSet, basename='Igreja')
router.register('cult', CultViewSet, basename='Culto')
router.register('function', FunctionViewSet, basename='Funcao')
router.register('member', MemberViewSet, basename='Membro')

# Rotas de Music
router.register('music', MusicViewSet, basename='Musica')
router.register('music-chord', MusicChordViewSet, basename='Acorde')
router.register('version-music', VersionMusicViewSet, basename='Versoes')
router.register('playlist', PlaylistViewSet, basename='Playlist')

# Rotas de Praise
router.register('cast', CastViewSet, basename='Escalacao')

# Rotas de User
router.register('user', UserViewSet, basename='Usuario')

# Documentação
schema_view = get_schema_view(
   openapi.Info(
      title="API de Gerenciamento do louvor",
      default_version='v1',
      description="Organizador das musicas e gerenciamento de escalações do louvor da igreja",
      terms_of_service="#",
      contact=openapi.Contact(email="wilian.santos.dev@outlook.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('gerenciamento-louvor-admin/', admin.site.urls),

    path('', include(router.urls)),
    #path('', include('apps.user.urls')),

    path('cult/<int:pk>/church/', ListCultChurch.as_view()),

    path('version-music/<int:pk>/music/', ListVersionMusic.as_view()),

    path('api/auth/', include('knox.urls')),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
