from django.contrib import admin

from . models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_filter = ('user',)
    search_fields = ('title', 'imageDescription')
    list_per_page = 25


admin.site.register(Image, ImageAdmin)
