from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from apps.church.views import ChurchViewSet, CultViewSet, ListCultChurch

router = routers.DefaultRouter()
router.register('church', ChurchViewSet, basename='Igreja')
router.register('cult', CultViewSet, basename='Culto')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('cult/<int:pk>/church/', ListCultChurch.as_view()),
]
