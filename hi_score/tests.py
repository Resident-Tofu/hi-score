from django.test import TestCase
from django.contrib.auth.models import User
from hi_score.models import UserProfile, Genre, Game, Review

class ReviewMethodTests(TestCase):

    def test_ensure_review_rating_between_one_and_five(self):
        u1 = User(username = "user1", password = "SomePass#1")
        u1.save()
        u2 = User(username = "user2", password = "SomePass#2")
        u2.save()
        u3 = User(username = "user3", password = "SomePass#3")
        u3.save()
        up1 = UserProfile(user = u1, rating = 1)
        up1.save()
        up2 = UserProfile(user = u2, rating = 2)
        up2.save()
        up3 = UserProfile(user = u3, rating = 3)
        up3.save()

        genre = Genre(name = "Genre")
        genre.save()
        game = Game(name = "Game", desc = "Hmm")
        game.save()
        game.genres.add(genre)
        game.save()

        review1 = Review(user = up1, game = game)
        review1.title = "Title1"
        review1.body = "Blah"
        review1.rating = 0
        review1.save()

        review2 = Review(user = up2, game = game)
        review1.title = "Title2"
        review1.body = "Bleh"
        review1.rating = 6
        review1.save()

        review3 = Review(user = up3, game = game)
        review3.title = "Title3"
        review3.body = "Bluh"
        review3.rating = -1
        review3.save()

        self.assertEqual((review1.rating >= 1 and review1.rating <= 5), True)
        self.assertEqual((review2.rating >= 1 and review1.rating <= 5), True)
        self.assertEqual((review3.rating >= 1 and review1.rating <= 5), True)