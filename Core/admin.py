from django.contrib import admin
from .models import *

class MidiaInline(admin.StackedInline):
    model = Midia_i
    extra = 1


class PlayoutAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'created_at', 'update_at']
    inlines = [MidiaInline]

class MidiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'duracao', 'nome_arquivo', 'created_at', 'update_at']


admin.site.register(Playout, PlayoutAdmin)
admin.site.register(Midia, MidiaAdmin)
