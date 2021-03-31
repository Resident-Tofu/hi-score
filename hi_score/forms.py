from django import forms
from django.contrib.auth.models import User
from hi_score.models import Game, Genre, Review, UserProfile
from hi_score.models import User


class GenreForm(forms.ModelForm):
	name = forms.CharField(max_length=32, help_text="Name:")
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Genre
		fields = ('name', )

class GameForm(forms.ModelForm):
	name = forms.CharField(max_length = 128, help_text="Name:")
	#TODO Nice dropdown list for genres, button to add another
	genres = forms.CharField(max_length = 64, help_text="Genre:")
	desc = forms.CharField(widget=forms.Textarea, help_text="Description:")
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Game
		fields = ('name', 'desc')

class ReviewForm(forms.ModelForm):
	title = forms.CharField(help_text="Review Title:")
	rating = forms.IntegerField(help_text = "Rating:")
	ytlink = forms.URLField(help_text = "Youtube Link:", required=False)

	class Meta:
		model = Review
		fields = ('title', 'body', 'rating', 'ytlink' )

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length = 64)
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password', )

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('aboutme', 'picture', )

