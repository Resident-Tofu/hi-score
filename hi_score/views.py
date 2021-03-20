from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the home Page!")

def about(request):
	return HttpResponse("This is the about page")

def faq(request):
	return HttpResponse("This is the Frequently asked questions")

def contact_us(request):
	return HttpResponse("This is the contact-us page")

def show_games(request):
	return HttpResponse("This is the games page")

def show_game(request, game_name_slug):
	return HttpResponse(f"This is the page for {game_name_slug}")

# Login Required
def review_game(request, game_name_slug):
	return HttpResponse(f"This is the {game_name_slug} review page")

# Login Required
def add_game(request):
	return HttpResponse("This is the add game page")

def show_genres(request):
	return HttpResponse("This is the genres page")

def add_genre(request):
	return HttpResponse("This is the add genre pages")

def show_genre(request, genre_name_slug):
	return HttpResponse(f"This is the {genre_name_slug} genre page")

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
