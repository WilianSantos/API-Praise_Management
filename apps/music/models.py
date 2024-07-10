from django.db import models

class MusicChord(models.Model):
    chord = models.CharField(max_length=10, null=False, blank=False)
    chord_image = models.ImageField(upload_to="chord_image/%Y/%m/%d/", blank=True)

    def __str__(self):
        return self.chord


class Music(models.Model):
    title_music = models.CharField(max_length=100, null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    music_text = models.TextField(null=False, blank=False)
    theme = models.CharField(max_length=50, null=True)
    music_chord = models.ManyToManyField(MusicChord)

    def __str__(self) -> str:
        return self.title


class VersionMusic(models.Model):
    author = models.CharField(max_length=100, null=False, blank=False)
    music_link = models.URLField(max_length=255, blank=True)
    music = models.ForeignKey(
        to=Music,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name='version_music'
    )

    def __str__(self) -> str:
        return self.author


class Playlist(models.Model):
    music = models.ManyToManyField(Music)
