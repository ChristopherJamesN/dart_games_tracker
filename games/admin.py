from django.contrib import admin

from .models import Game, Player


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 4


class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['max_score']}),
        ('Date information', {'fields': ['game_date']}),
    ]
    inlines = [PlayerInline]
    list_display = ('max_score', 'game_date')


admin.site.register(Game, GameAdmin)
