from django.db import models

from apps.church.models import Church, Cult
from apps.music.models import Playlist


class FunctionPraise(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class MemberPraise(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    function = models.ManyToManyField(FunctionPraise)
    availability = models.BooleanField(default=True)
    cell_phone = models.CharField(max_length=14)
    is_member = models.BooleanField(default=False)
    church = models.OneToOneField(
        to=Church,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='member_praise_church'
    )

    def __str__(self) -> str:
        return self.name
    

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
    guitar = models.OneToOneField(
        to=MemberPraise,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='guitar_cast'
    )
    electric_guitar = models.OneToOneField(
        to=MemberPraise,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='electric_guitar_cast'
    )
    musical_keyboard = models.OneToOneField(
        to=MemberPraise,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='musical_keyboard_cast'
    )
    low = models.OneToOneField(
        to=MemberPraise,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='low_cast'
    )
    drums = models.OneToOneField(
        to=MemberPraise,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='drums_cast'
    )
    vocal = models.ManyToManyField(MemberPraise, related_name='vocal_cast')

    def __str__(self) -> str:
        return self.cult
