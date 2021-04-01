from django.test import TestCase
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

    def test_slug_line_creation(self):
        """
        Checks that appropriate slugs for urls are created.
        """
        genre = add_genre("Role Playing Game")
        game = add_game("X_Power Chronicles", (genre,))

        self.assertEqual(genre.slug, "role-playing-game")
        self.assertEqual(game.slug, "x_power-chronicles")

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