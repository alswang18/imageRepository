from django.contrib import admin

from . models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'hidden_to_others', 'copyrighted')
    list_filter = ('user',)
    list_editable = ('hidden_to_others', 'copyrighted')
    search_fields = ('title', 'imageDescription')
    list_per_page = 25


admin.site.register(Image, ImageAdmin)
