from django.contrib import admin
from places.models import Excursion, Image

# Register your models here.

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

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
