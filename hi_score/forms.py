from django import forms
from django.contrib.auth.models import User
from hi_score.models import Game, Genre, Review
from hi_score.models import User


class GenreForm(forms.ModelForm):
	name = forms.CharField(max_length=32, help_text="Please enter the genre name.")
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Genre
		fields = ('name', )

class GameForm(forms.ModelForm):
	pass
#  	user = forms.OneToOneField(User, on_delete = models.CASCADE)
#     username = forms.CharField(max_length = 32)
#     password = forms.CharField(max_length = 32)
#     picture = forms.ImageField(upload_to = 'profile_images', blank = True)
#     aboutme = forms.TextField(blank = True)
#     datejoined = forms.DateField()
#     rating = forms.DecimalField(decimal_places = 2, max_digits = 3)

class UserForm(forms.ModelForm):
	pass

class UserProfileForm(forms.ModelForm):
	pass