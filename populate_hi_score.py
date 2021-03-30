import os
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "hiscore_project.settings"
)

import django
django.setup()
from hi_score.models import UserProfile, Genre, Game, Review
from django.contrib.auth.models import User
from datetime import date

def populate():
    users = [
    #     {
    #         "username": "Rex",
    #         "password": "okay123",
    #         "aboutme": "I just like games",
    #         "rating": 4,
    #     }
    ]

    genre_pages = [
        { "name": "Action" },
        { "name": "Adventure" },
        { "name": "Racing" },
        { "name": "Sports" },
        { "name": "Shooter" },
        { "name": "Platformer" },
        { "name": "Puzzle" },
        { "name": "RPG" },
        { "name": "Fighting" },
        { "name": "Strategy" },
    ]

    game_pages = [
        {
            "name": "Crash Bandicoot",
            "genres": { "Platformer" },
            "desc": "The orange marsupial jumps through platforming challenges.",
        },
        {
            "name": "The Witness",
            "genres": { "Puzzle" },
            "desc": "Solve the mystery of the island by tracing lines on panels.",
        },
        { 
            "name": "Rayman",
            "genres": { "Platformer", "Adventure" },
            "desc": "Save the world as the limbless hero.",
        },
        {
            "name": "Uncharted",
            "genres": { "Action", "Adventure", "Shooter" },
            "desc": "Nathan Drake globetrots for treasure.",
        },
        {
            "name" : "Halo",
            "genres": { "Action", "Shooter" },
            "desc" : "Shoot aliens on a big ring.",
        },
        {
            "name" : "Wipeout",
            "genres": { "Racing" },
            "desc" : "Zip through gravity-defying courses in this futuristic racer.",
        },
        {
            "name" : "Warcraft",
            "genres": { "Strategy" },
            "desc" : "Vanquish your foes by commanding units in this timeless classic.",
        },
        {
            "name" : "Tekken",
            "genres": { "Fighting" },
            "desc" : "Beat up all others in the Iron Fist Tournament.",
        },
        {
            "name" : "Doom Eternal",
            "genres": { "Action", "Shooter" },
            "desc" : "Give those demons Hell.",
        },
    ]

    reviews = [
    #     {
    #         "game": "The Witness",
    #         "title": "Mindblowing",
    #         "user"
    #         "rating": 4,
    #         "likes": 297,
    #         "dislikes": 53,
    #         "body": "This game changed how I played games forever.  Initially, I was sceptical, but I persisted and discovered hidden depth to this game.  It is a guided meditation that leads to a small inner awakening.  Can't recommend enough.",
    #         "captions": False,
    #     },
    #     {
    #         "game": "The Witness",
    #         "title": "What",
    #         "rating": 1,
    #         "likes": 45,
    #         "dislikes": 36,
    #         "body": "No idea why I let people talk me into buying this humongous waste of time -- avoid",
    #         "captions": False,
    #     },
    #     {
    #         "game": "Doom Eternal",
    #         "title": "RIP AND TEAR",
    #         "rating": 5,
    #         "likes": 666,
    #         "dislikes": 9,
    #         "body": "SHOOT BIG GUN MAKE DEMONS GO EXPLODEY THIS GAME IS THE GOAT",
    #         "ytlink": "https://youtu.be/_bA3nM_v2eU",
    #         "captions": False,
    #     },
    ]

    # Create users
    for user in users:
        u, created = User.objects.get_or_create(username = user["username"])
        if not created:
            u.set_password(user["password"])
        u.save()
        up = UserProfile(user = u, aboutme = user["aboutme"], rating = user["rating"])
        up.datejoined = date.today()
        up.save()

    # Create the genre pages
    for genre in genre_pages:
        g = Genre.objects.get_or_create(name = genre["name"])[0]
        g.save()

    # Create the game pages
    for game in game_pages:
        g = Game.objects.get_or_create(name = game["name"], desc = game["desc"])[0]
        for genre in game["genres"]:
            g.genres.add(Genre.objects.get(name = genre))
        g.save()

    # Create the reviews
    for review in reviews:
        r = Review(title = review["title"], game = Game.objects.get(name = review["game"]))
        r.rating = review.get("rating", 3) #review["rating"]
        r.likes = review.get("likes", 0)
        r.dislikes = review.get("dislikes", 0)
        r.ytlink = review.get("ytlink", "")
        if r.ytlink:
            r.embed = "https://www.youtube.com/embed/" + r.ytlink[r.ytlink.rfind("/"):]
        if r.ytlink and review.get("captions") == True:
                pass # Use YouTube API to get captions, use as review body
        else:
            r.body = review.get("body", "")
        r.save()


# Execution
if __name__ == "__main__":
    print("Populating Hi-Score database...")
    populate()
