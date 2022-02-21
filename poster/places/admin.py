from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.conf import settings

from places.models import Excursion, Image
from adminsortable2.admin import SortableInlineAdminMixin


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'sort_index',)

    def get_preview(self, obj, width=200):
        return format_html(
            '<img src="{}" width="{}" />',
            mark_safe(obj.photo.url),
            width
        )
    get_preview.short_description = 'ИЗОБРАЖЕНИЕ'


class ExcursionAdmin(admin.ModelAdmin):
    # форма элемента
    fieldsets = [
        (None,         {'fields': ['title']}),
        ('Описание',   {'fields': ['description_short',
         'description_long'], 'classes': ['collapse']}),
        ('Координаты', {'fields': ['lat', 'lon'], 'classes': ['collapse']}),
    ]
    search_fields = ['title']
    inlines = [ImageInline]


admin.site.register(Excursion, ExcursionAdmin)
if settings.DEBUG:
    admin.site.register(Image)
