from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from hi_score.models import Genre
from hi_score.models import Game
from hi_score.models import Review
from hi_score.forms import UserForm, UserProfileForm
from hi_score.forms import GenreForm, GameForm

def index(request):
	genre_list = Genre.objects.order_by("-name")[:10]
	game_list = Game.objects.order_by("-name")[:5]
	context_dict = {}
	context_dict["genres"] = genre_list
	context_dict["games"] = game_list
	response = render(request, "hi-score/home.html", context=context_dict)
	return response

def about(request):
	return render(request, 'hi-score/about.html')

def faq(request):
	return render(request, 'hi-score/faq.html')

def contact_us(request):
	return render(request, 'hi-score/contact_us.html')

def show_games(request):
	game_list = Game.objects.order_by("-name")
	for i in game_list:
		print(i.name)
	context_dict = {"games": game_list}
	response = render(request, 'hi-score/games.html', context=context_dict)
	return response

def show_game(request, game_name_slug):
	game = Game.objects.get(slug = game_name_slug)
	context_dict = {}
	context_dict["name"] = game.name
	#context_dict["genres"] = game.genres
	context_dict["desc"] = game.desc
	review_list = Review.objects.filter(game = game)
	context_dict["reviews"] = review_list

	return render(request, 'hi-score/game.html', context=context_dict)

# Login Required
def review_game(request, game_name_slug):
	return render(request, 'hi-score/review_game.html')

# Login Required
def add_game(request):
	form = GameForm()

	# A HTTP POST?
	if request.method == 'POST':
		form = GameForm(request.POST)

	if form.is_valid():
		form.save(commit=True)
		return redirect(reverse('hi-score:show_games'))

	else:
		# Form had errors, print to terminal
		print(form.errors)

	return render(request, 'hi-score/add_game.html', {'form': form})

def show_genres(request):
	genre_list = Genre.objects.order_by('-name')
	context_dict = {'genres': genre_list}
	return render(request, 'hi-score/genres.html', context=context_dict)

def add_genre(request):
	form = GenreForm()

	# A HTTP POST?
	if request.method == 'POST':
		form = GenreForm(request.POST)

	if form.is_valid():
		form.save(commit=True)
		return redirect(reverse('hi-score:genres'))

	else:
		# Form had errors, print to terminal
		print(form.errors)

	return render(request, 'hi-score/add_genre.html', {'form': form})


def show_genre(request, genre_name_slug):
	#genre_info = None#Genre.name
	#game_list = None#Game.objects.get(genre = genre.name)
	context_dict = {}
	try:
		genre = Genre.objects.get(slug = genre_name_slug)
		games = Game.objects.filter(genres = genre)
		context_dict['genre'] = genre
		context_dict['games'] = games
	except Genre.DoesNotExist:
		context_dict['genre'] = None
		context_dict['games'] = None
	return render(request, 'hi-score/genre.html', context=context_dict)


def signup(request):
	registered = False

	# If it's a http POST, process form data
	if request.method == 'POST':
		# Retrieve data from the forms
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			# Save the form data to the database
			user = user_form.save()

			# set_password hashes the password, then we save the user
			user.set_password(user.password)
			user.save()

			# commit=False delays saving the model to avoid integrity issues
			# Create the one-to-one relationship between the profile and user
			profile = profile_form.save(commit=False)
			profile.user = user

			# If user uploaded a picture, add it, then save profile to db
			if 'picture' in request.FILES:
				profile_picture = request.FILES['picture']

				profile.save()
				# At this point, user is registered
			registered = True
		else:
			# Display errors
			print(user_form.errors, profile_form.errors)

	else:
		# Render using Blank forms ready for user input
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render(request,
			'hi-score/enlist.html',
			context = {'user_form': user_form,
					   'profile_form': profile_form,
					   'registered': registered})


def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		# Check if username/password combination is valid, returns a User obj
		user = authenticate(username=username, password=password)

		# If above was valid
		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse('hi-score:home'))
			else:
				return HttpResponse('Your Hi-Score account is disabled.')
		else:
			# Bad login details were provided
			print(f'Invalid login details {username}, {password}')
			return HttpResponse('Invalid login details supplied.')
	else:
		return render(request, 'hi-score/login.html')

# Login Required
def show_account(request):
	return HttpResponse("This is the myaccount page")

# Login Required
def user_logout(request):
	return HttpResponse("This is the user-logout view")
