from django.contrib import admin
from hi_score.models import Genre, Game, Review

# Register your models here.
admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(Review)