from django.shortcuts import render
from django.http import HttpResponse
from hi_score.models import Genre
from hi_score.models import Game
from hi_score.models import Review

def index(request):
	# Context Dict
	# -Top 10 genres
	# -Top 5 newest/best games
	genre_list = Genre.objects.order_by("-name")[:10]
	game_list = Game.objects.order_by("-name")[:5]
	context_dict = {}
	context_dict["genres"] = genre_list
	context_dict["games"] = game_list
	response = render(request, 'hi-score/index.html', context=context_dict)
	return response
	# return HttpResponse("hi")

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
	context_dict = {}
	review_list = Review.objects.filter()

	return render(request, 'hi-score/game.html', context=context_dict)

# Login Required
def review_game(request, game_name_slug):
	return render(request, 'hi-score/review_game')

# Login Required
def add_game(request):
	return render(request, 'hi-score/add_game')

def show_genres(request):
	genre_list = Genre.objects.order_by('-name')
	context_dict = {'genres': genre_list}
	return render(request, 'hi-score/genres', context=context_dict)

def add_genre(request):
	return render(request, 'hi-score/add_genre')

def show_genre(request, genre_name_slug):
	genre_info = None#Genre.name
	game_list = None#Game.objects.get(genre = genre.name)
	context_dict = {}
	context_dict['genre'] = genre_info
	context_dict['games'] = game_list
	return render(request, 'hi-score/genre', context=context_dict)

def signup(request):
	return HttpResponse("This is the signup page")

def user_login(request):
	return HttpResponse("This is the login page")

# Login Required
def show_account(request):
	return HttpResponse("This is the myaccount page")

# Login Required
def user_logout(request):
	return HttpResponse("This is the user-logout view")
