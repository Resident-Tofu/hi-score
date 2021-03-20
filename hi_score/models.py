from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     # Review User class
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     username = models.CharField(max_length = 32)
#     password = models.CharField(max_length = 32)
#     picture = models.ImageField(upload_to = 'profile_images', blank = True)
#     aboutme = models.TextField(blank = True)
#     datejoined = models.DateField()
#     rating = models.DecimalField(decimal_places = 2, max_digits = 3)

#     def __str__(self):
#         return self.user.username

class Genre(models.Model):
    name = models.CharField(max_length = 32, unique = True)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    genres = models.ManyToManyField(Genre)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    title = models.CharField(max_length = 32)
    body = models.TextField()
    date = models.DateField(auto_now = True) # using over `auto_now_add` to update on user edit
    rating = models.PositiveSmallIntegerField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    ytlink = models.URLField(default = None, null = True, unique = True) # Validate using forms
    captions = models.BooleanField(default = False) # If true, use video captions as body of review

    def save(self, *args, **kwargs):
        if self.ytlink == "":
            self.ytlink = None
        super(Review, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title