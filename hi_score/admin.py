from django.contrib import admin
from hi_score.models import Genre, Game, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "game", "date")

# Register your models here.
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Review, ReviewAdmin)