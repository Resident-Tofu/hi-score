from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from hi_score.models import UserProfile, Genre, Game, Review

# Helper functions
def add_user(name):
    user = User(username = name, password = "SomePassWord#123")
    user.save()
    userpro = UserProfile(user = user, rating = 3)
    userpro.save()
    return userpro

def add_genre(name):
    genre = Genre(name = name)
    genre.save()
    return genre

def add_game(name, genres):
    game = Game(name = name, desc = "Some game description")
    game.save()
    for genre in genres:
        game.genres.add(genre)
    game.save()
    return game

def add_review(user, game):
    review = Review(user = user, game = game)
    review.title = "Some Review Title"
    review.body = "Some game review"
    review.rating = 3
    review.save()
    return review


class ReviewMethodTests(TestCase):
    def test_ensure_review_rating_between_one_and_five(self):
        """
        Ensures the rating for a review is between 1 and 5.
        """
        user1 = add_user("user1")
        user2 = add_user("user2")
        user3 = add_user("user3")

        genre = add_genre("Genre")
        game = add_game("Game", (genre,))

        review1 = add_review(user1, game)
        review2 = add_review(user2, game)
        review3 = add_review(user3, game)

        self.assertEqual((review1.rating >= 1 and review1.rating <= 5), True)
        self.assertEqual((review2.rating >= 1 and review1.rating <= 5), True)
        self.assertEqual((review3.rating >= 1 and review1.rating <= 5), True)


class GenreMethodTests(TestCase):

    def test_slug_line_creation(self):
        """
        Checks that appropriate slugs for urls are created.
        """
        genre = add_genre("Role Playing Game")

        self.assertEqual(genre.slug, "role-playing-game")


class GameMethodTests(TestCase):

    def test_slug_line_creation(self):
        """
        Checks that appropriate slugs for urls are created.
        """
        genre = add_genre("Role Playing Game")
        game = add_game("X_Power Chronicles", (genre,))

        self.assertEqual(game.slug, "x_power-chronicles")


class GenreViewTests(TestCase):

    def test_genres_page_no_genres(self):
        """
        Check the genres page displays an appropriate message when there are no genres
        """
        response = self.client.get(reverse("hi-score:genres"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no genres yet.  Add the first!")
        self.assertQuerysetEqual(response.context["genres"], [])

    def test_genres_page_with_genres(self):
        """
        Check the genres page displays genres
        """
        add_genre("Role Playing Game")
        add_genre("Action")
        add_genre("Sports")

        response = self.client.get(reverse("hi-score:genres"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Role Playing Game")
        self.assertContains(response, "Action")
        self.assertContains(response, "Sports")

        num_genres = len(response.context["genres"])
        self.assertEqual(num_genres, 3)


class GameViewTests(TestCase):

    def test_games_page_no_games(self):
        """
        Check the games page displays an appropriate message when there are no genres
        """
        response = self.client.get(reverse("hi-score:show_games"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no games yet.  Add the first!")
        self.assertQuerysetEqual(response.context["games"], [])

    def test_games_page_with_games(self):
        """
        Check the games page displays games
        """
        add_game("Crash Bandicoot", (add_genre("Platformer"),))
        add_game("Wipeout", (add_genre("Racing"),))
        add_game("Super Smash Bros", (add_genre("Fighting"), add_genre("Party")))

        response = self.client.get(reverse("hi-score:show_games"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Crash Bandicoot")
        self.assertContains(response, "Wipeout")
        self.assertContains(response, "Super Smash Bros")

        num_genres = len(response.context["games"])
        self.assertEqual(num_genres, 3)