from django import forms
from django.contrib.auth.models import User
from hi_score.models import Game, Genre, Review
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

class UserForm(forms.ModelForm):
	pass

class UserProfileForm(forms.ModelForm):
	pass