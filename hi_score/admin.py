from django.contrib import admin
from hi_score.models import Genre, Game, Review, UserProfile

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "game", "date")

class GameInline(admin.TabularInline):
    model = Game.genres.through
    extra = 1

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        GameInline,
    ]

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        GameInline,
    ]
    exclude = ("genres",)

class ProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    

# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile, ProfileAdmin)
