from django.db import models

from apps.church.models import Cult, Member
from apps.music.models import Playlist
    

class Cast(models.Model):
    cult = models.OneToOneField(
        to=Cult,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='cult_cast'
    )
    playlist = models.OneToOneField(
        to=Playlist,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='playlist_cast'
    )
    members = models.ManyToManyField(Member)
