from django.test import TestCase
from hi_score.models import UserProfile, Genre, Game, Review

class ReviewMethodTests(TestCase):

    def test_ensure_review_rating_between_one_and_five(self):
        user1 = UserProfile(user = User(username = "user1"))
        user1.save()
        user2 = UserProfile(user = User(username = "user2"))
        user2.save()
        user3 = UserProfile(user = User(username = "user3"))
        user3.save()

        genre = Genre("Genre")
        genre.save()
        game = Game(name = "Game", genre = genre, desc = "Hmm")
        game.save()

        review1 = Review(user = user1, game = game)
        review1.title = "Title1"
        review1.body = "Blah"
        review1.rating = 0
        review1.save()

        review2 = Review(user = user2, game = game)
        review1.title = "Title2"
        review1.body = "Bleh"
        review1.rating = 6
        review1.save()

        review3 = Review(user = user3, game = game)
        review3.title = "Title3"
        review3.body = "Bluh"
        review3.rating = -1
        review3.save()

        self.assertEqual((review1.rating >= 1 and review1.rating <= 5), True)
        self.assertEqual((review2.rating >= 1 and review1.rating <= 5), True)
        self.assertEqual((review3.rating >= 1 and review1.rating <= 5), True)