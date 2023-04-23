from django.contrib import admin
from .models import *


class TvAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'time_create', 'is_published', 'photo', 'model')
    list_display_links = ('title',)
    list_editable = ('is_published', 'model')
    list_filter = ('is_published', 'time_create')


admin.site.register(Tv, TvAdmin)
admin.site.register(Model)
