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
        {
            "username": "Rex",
            "password": "okay123",
            "aboutme": "I just like games",
            "rating": 4,
        },
        {
            "username": "Peach73",
            "password": "sprinkles",
            "aboutme": "",
            "rating": 3,
        },
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
        {
            "game": "The Witness",
            "title": "Mindblowing",
            "user": "Rex",
            "rating": 4,
            "likes": 297,
            "dislikes": 53,
            "body": "This game changed how I played games forever.  Initially, I was sceptical, but I persisted and discovered hidden depth to this game.  It is a guided meditation that leads to a small inner awakening.  Can't recommend enough.",
            "captions": False,
        },
        {
            "game": "The Witness",
            "title": "What",
            "user": "Peach73",
            "rating": 1,
            "likes": 45,
            "dislikes": 36,
            "body": "No idea why I let people talk me into buying this humongous waste of time -- avoid",
            "captions": False,
        },
        {
            "game": "Doom Eternal",
            "title": "RIP AND TEAR",
            "user": "Rex",
            "rating": 5,
            "likes": 666,
            "dislikes": 9,
            "body": "SHOOT BIG GUN MAKE DEMONS GO EXPLODEY THIS GAME IS THE GOAT",
            "ytlink": "https://youtu.be/_bA3nM_v2eU",
            "captions": False,
        },
        {
            "game": "Doom Eternal",
            "title": "Video Review!",
            "user": "Peach73",
            "rating": 3,
            "likes": 3,
            "dislikes": 3,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/vqduGTChT5U",
            "captions": True,
        },
        {
            "game": "Halo",
            "title": "Its a 10!!",
            "user": "Rex",
            "rating": 5,
            "likes": 291,
            "dislikes": 5,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/njLsiNmQ5tI",
            "captions": True,
        },
        {
            "game": "Tekken",
            "title": "Tekken 7 is a love letter to this long-running franchise",
            "user": "Peach73",
            "rating": 4,
            "likes": 340,
            "dislikes": 75,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/TwFmJQPIZcA",
            "captions": True,
        },
        {
            "game": "Crash Bandicoot",
            "title": "Games like this that keep me coming back to steam! ",
            "user": "Peach73",
            "rating": 4,
            "likes": 120,
            "dislikes": 17,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/AW2EEoW_Tw4",
            "captions": True,
        },
        {
            "game": "Rayman",
            "title": "I hate this game with all my soul ",
            "user": "Rex",
            "rating": 2,
            "likes": 120,
            "dislikes": 259,
            "body": "Theres a reason no-one plays this game anymore and the awful graphics are the main factor :(  ",
            "captions": False,
        },
        {
            "game": "Uncharted",
            "title": "My favourite game/series of ALL TIME! 50 years from now I will still play Uncharted ;)",
            "user": "Peach73",
            "rating": 5,
            "likes": 560,
            "dislikes": 25,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/ntCFRWahdpU",
            "captions": True,
        },
        {
            "game": "Warcraft",
            "title": "strange that dungeons, raids or PvP was not really touched on at all...",
            "user": "Peach73",
            "rating": 4,
            "likes": 56,
            "dislikes": 2,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/5Er0UyHPLp8",
            "captions": True,
        },
        {
            "game": "Wipeout",
            "title": "One Of The Best Racing Games Released In Years",
            "user": "Rex",
            "rating": 5,
            "likes": 356,
            "dislikes": 27,
            "body": "This should not show up.",
            "ytlink": "https://youtu.be/zIpQ50AV8Rk",
            "captions": True,
        },
        {
            "game": "Wipeout",
            "title": "I love speeeeed",
            "user": "Peach73",
            "rating": 4,
            "likes": 35,
            "dislikes": 7,
            "body": "I think the think I loved the most about WipEout was the semi-realistic presentation of it all. The way you've got all these teams, with their own distinct logos on their ships, ads plastered all over the tracks and on billboards surrounding them...the artwork of The Designers Republic really brought this world to life ",
            "captions": False,
        },
        {
            "game": "Wipeout",
            "title": "Different review",
            "user": "Peach73",
            "rating": 4,
            "likes": 35,
            "dislikes": 7,
            "body": "Should not see this since only one review per user on a game",
            "captions": False,
        },
    ]

    # Create users
    for user in users:
        u, created = User.objects.get_or_create(username = user["username"])
        if created:
            u.set_password(user["password"])
        u.save()
        up = UserProfile()
        up.user = u
        up.aboutme = user["aboutme"]
        up.rating = user["rating"]
        up.datejoined = date.today()
        up.save()
    # u, created = User.objects.get_or_create(username = "Rex")
    # if created:
    #     u.set_password(123)
    # u.save()
    # up = UserProfile()
    # up.user = u
    # up.aboutme = "I just wanna play some games"
    # up.rating = 2.0
    # up.datejoined = date.today()
    # up.picture = get_profile_pic("amogus.jpg")
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
        u = User.objects.get(username = review["user"])
        up = UserProfile.objects.get(user = u)
        g = Game.objects.get(name = review["game"])
        r, created = Review.objects.get_or_create(user = u, game = g)
        if created:
            r.title = review["title"]
            r.rating = review.get("rating", 3) #review["rating"]
            r.likes = review.get("likes", 0)
            r.dislikes = review.get("dislikes", 0)
            r.ytlink = review.get("ytlink", "")
            r.captions = review.get("captions", False)
            if r.ytlink:
                r.embed = "https://www.youtube.com/embed/" + r.ytlink[r.ytlink.rfind("/") + 1:]
            r.body = "" if r.captions else review.get("body", "") # Otherwise, use AJAX to handle captions
            r.save()

def get_profile_pic(name):
    return f'{os.getcwd()}/media/profile_images/{name}'

# Execution
if __name__ == "__main__":
    print("Populating Hi-Score database...")
    populate()
