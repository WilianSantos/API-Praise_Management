from django.contrib import admin

from .models import Music, MusicChord, VersionMusic, Playlist


class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_music', 'author', 'theme',)
    list_display_links = ('id', 'title_music', 'author',)
    search_fields = ('title_music', 'author', 'theme', 'category')
    list_filter = ('title_music', 'author', 'theme', 'category')
    list_per_page = 10
    ordering = ('title_music',)

admin.site.register(Music, MusicAdmin)


class MusicChordAdmin(admin.ModelAdmin):
    list_display = ('chord',)
    list_display_links = ('chord',)
    search_fields = ('chord',)
    list_filter = ('chord',)
    list_per_page = 10
    ordering = ('chord',)

admin.site.register(MusicChord, MusicChordAdmin)


class VersionMusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'music',)
    list_display_links = ('id', 'author', 'title',)
    search_fields = ('author', 'title', 'music',)
    list_filter = ('author', 'title', 'music',)
    list_per_page = 10
    ordering = ('author',)

admin.site.register(VersionMusic, VersionMusicAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date',)
    list_display_links = ('id', 'name', 'date',)
    search_fields = ('name', 'date',)
    list_filter = ('name', 'date',)
    list_per_page = 10
    ordering = ('date',)

admin.site.register(Playlist, PlaylistAdmin)
