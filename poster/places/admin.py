from django.contrib import admin
from django.utils.html import format_html
from places.models import Excursion, Image

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'sort_index',)

    def get_preview(self, obj, width=200):
        return format_html(
            f'<img src="{obj.photo.url}" width="{width}" />'
        )


class ExcursionAdmin(admin.ModelAdmin):
    # форма элемента
    fieldsets = [
        (None,         {'fields': ['title']}),
        ('Описание',   {'fields': ['description_short', 'description_long'], 'classes': ['collapse']}),
        ('Координаты', {'fields': ['lat', 'lon'], 'classes': ['collapse']}),
    ]
    inlines = [ImageInline]


admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Image)
