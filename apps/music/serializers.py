from rest_framework import serializers

from .models import Music, MusicChord, VersionMusic, Playlist


class MusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = '__all__'


class VersionMusicSerializers(serializers.ModelSerializer):
    class Meta:
        model = VersionMusic
        fields = '__all__'

class ListVersionMusicSerializer(serializers.ModelSerializer):
    music = serializers.ReadOnlyField(source='music.title_music')

    class Meta:
        model = VersionMusic
        fields = ['music', 'author', 'music_link']


class MusicChordSerializers(serializers.ModelSerializer):
    class Meta:
        model = MusicChord
        fields = '__all__'


class PlaylistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'
