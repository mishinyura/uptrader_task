from django.contrib import admin
from .models import Link, Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'
    list_display_links = 'pk', 'name'
    ordering = 'pk',

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'url', 'position'
    list_display_links = 'pk', 'name'
    ordering = 'pk',
