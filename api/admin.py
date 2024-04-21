from django.contrib import admin

from .models import TextFile


@admin.register(TextFile)
class TextFileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'data')
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'