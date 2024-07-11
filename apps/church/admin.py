from django.contrib import admin

from .models import Church, Cult

class ChurchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    list_per_page = 5
    ordering = ('name',)


admin.site.register(Church, ChurchAdmin)


class CultAdmin(admin.ModelAdmin):
    list_display = ('id', 'theme', 'date', 'preacher', 'church')
    list_display_links = ('id', 'theme', 'preacher')
    search_fields = ('theme', 'preacher',)
    list_filter = ('theme', 'preacher', )
    list_per_page = 10
    ordering = ('date',)


admin.site.register(Cult, CultAdmin)

