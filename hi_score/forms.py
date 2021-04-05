import re
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
	genres = forms.ModelMultipleChoiceField(queryset = Genre.objects.all(), help_text="Genre:", widget = forms.CheckboxSelectMultiple)
	desc = forms.CharField(widget=forms.Textarea, help_text="Description:")
	image = forms.ImageField(help_text="Picture:", required=False)
	slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Game
		fields = ('name', 'desc', 'genres', 'image')

class ReviewForm(forms.ModelForm):
	RATINGS = []
	for i in range(1, 6):
		RATINGS.append((i, i * "⭐"))
	title = forms.CharField(help_text="Review Title:")
	rating = forms.IntegerField(help_text = "Rating:", widget = forms.RadioSelect(choices = RATINGS))
	ytlink = forms.URLField(help_text = "Youtube Link:", required=False)
	captions = forms.BooleanField(help_text = "Generate review from video captions?", required=False)

	def clean(self):
		super(ReviewForm, self).clean()

		ytlink = self.cleaned_data.get('ytlink')
		captions = self.cleaned_data.get('captions')
		if ytlink:
			match = re.match("(http(s)://www.youtube\.com/watch\?v=)([a-zA-Z0-9\-_])", ytlink)

			if not match:
				self._errors['ytlink'] = self.error_class(['Please enter a valid YouTube URL'])
		
		# If captions have been ticked, but no video has been provided
		elif captions:
			self._errors['captions'] = self.error_class(['No video URL has been provided'])

		return self.cleaned_data


	class Meta:
		model = Review
		fields = ('title', 'body', 'rating', 'ytlink', 'captions' )

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length = 64)
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('aboutme', 'picture', )

