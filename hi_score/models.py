from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    # Links UserProfile to an instance of User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile")
    aboutme = models.TextField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    datejoined = models.DateField()
    rating = models.DecimalField(decimal_places = 2, max_digits = 3)

class Genre(models.Model):
    name = models.CharField(max_length = 32, unique = True)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    genres = models.ManyToManyField(Genre)
    desc = models.TextField()
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Game, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 32, unique = True)
    body = models.TextField()
    date = models.DateField(auto_now = True) # using over `auto_now_add` to update on user edit
    rating = models.PositiveSmallIntegerField()
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()
    ytlink = models.URLField(default = None, null=True, blank=True) # Validate using forms
    embed = models.CharField(max_length = 128, default = None, null = True, blank = True)
    captions = models.BooleanField(default = False) # If true, use video captions as body of review

    def save(self, *args, **kwargs):
        if self.ytlink == "":
            self.ytlink = None

        super(Review, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
