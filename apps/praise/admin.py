from django.contrib import admin

from .models import Cast

class CastAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
    list_per_page = 10

admin.site.register(Cast, CastAdmin)
