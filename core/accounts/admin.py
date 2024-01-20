from django.contrib import admin
from .models import FavoriteNews


class FavoriteNewsAdmin(admin.ModelAdmin):
    list_display = ['user', 'favorite']


admin.site.register(FavoriteNews, FavoriteNewsAdmin)
