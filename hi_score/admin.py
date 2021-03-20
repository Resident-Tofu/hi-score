from django.contrib import admin
from hi_score.models import Genre, Game, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "game", "date")

class GameInline(admin.TabularInline):
    model = Game.genres.through
    extra = 1

class GenreAdmin(admin.ModelAdmin):
    inlines = [
        GameInline,
    ]

class GameAdmin(admin.ModelAdmin):
    inlines = [
        GameInline,
    ]
    exclude = ("genres",)

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Game)
admin.site.register(Review, ReviewAdmin)