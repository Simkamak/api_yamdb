from django.contrib import admin
from .models import Category, Title, Genre
from .resources import CategoryResource, GenreResource, TitleResource
from import_export.admin import ImportMixin


class CategoryAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    empty_value_display = '-пусто-'
    resource_class = CategoryResource


class GenreAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    empty_value_display = '-пусто-'
    resource_class = GenreResource


class TitleAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'description', 'category')
    empty_value_display = '-пусто-'
    resource_class = TitleResource


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
