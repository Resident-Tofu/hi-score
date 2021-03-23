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

class UserForm(forms.ModelForm):
	pass

class UserProfileForm(forms.ModelForm):
	pass