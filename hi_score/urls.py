from django.urls import path 
from hi_score import views

app_name = 'hi-score'

'''
/home 
/contact-us 
/faq 
/games
	/games/add-game 
	/games/game
		/games/game/review-game 
/genres
/genres/genre 
/signup
/login
/login/myaccount
'''

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('games/', views.show_games, name='show_games'),
    path('games/add-game', views.add_game, name='add_game'),
    path('games/<slug:game_name_slug>', views.show_game, name='show_game'),
    path('games/<game_name_slug>/review-game/', views.review_game, name='review_game'),
    path('genres/', views.show_genres, name='genres'),
    path('genres/add-genre', views.add_genre, name='add_genre'),
    path('genres/<slug:genre_name_slug>', views.show_genre, name='show_genre'),
    path('enlist/', views.signup, name='signup'),
    path('login/', views.user_login, name='user_login'),
    path('login/myaccount/', views.show_account, name='show_account'),
    path('logout/', views.user_logout, name='logout')


]