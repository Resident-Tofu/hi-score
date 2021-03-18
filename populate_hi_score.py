import os
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "hiscore_project.settings"
)

import django
django.setup()
from hi_score.models import Genre, Game, Review


def populate():
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
            "name" : "Crash Bandicoot",
            "genres": { "Platformer" },
            "desc" : "The orange marsupial jumps through platforming challenges."
        },
        {
            "name" : "The Witness",
            "genres": { "Puzzle" },
            "desc" : "Solve the mystery of the island by tracing lines on panels."
        },
        { 
            "name" : "Rayman",
            "genres": { "Platformer", "Adventure" },
            "desc" : "Save the world as the limbless hero."
        },
        {
            "name" : "Uncharted",
            "desc" : "Nathan Drake globetrots for treasure."
        },
        {
            "name" : "Halo",
            "genres": { "Action", "Shooter" },
            "desc" : "Shoot aliens on a big ring."
        },
        {
            "name" : "Wipeout",
            "genres": { "Racing" },
            "desc" : "Zip through gravity-defying courses in this futuristic racer."
        },
        {
            "name" : "Warcraft",
            "genres": { "Strategy" },
            "desc" : "Vanquish your foes by commanding units in this timeless classic."
        },
        {
            "name" : "Tekken",
            "genres": { "Fighting" },
            "desc" : "Beat up all others in the Iron Fist Tournament."
        },
    ]

    reviews = [
        {
            "game": "The Witness",
            "title": "Mindblowing",
            "rating": 4,
            "likes": 297,
            "dislikes": 53,
            "body": "This game changed how I played games forever.  Initially, I was sceptical, but I persisted and discovered hidden depth to this game.  It is a guided meditation that leads to a small inner awakening.  Can't recommend enough."
        },
        {
            "game": "The Witness",
            "title": "What",
            "rating": 1,
            "likes": 45,
            "dislikes": 36,
            "body": "No idea why I let people talk me into buying this humongous waste of time -- avoid"
        },
        {
            "game": "Doom Eternal",
            "title": "RIP AND TEAR",
            "rating": 5,
            "likes": 666,
            "dislikes": 9,
            "body": "SHOOT BIG GUN MAKE DEMONS GO EXPLODEY THIS GAME IS THE GOAT"
        },
    ]

    # Create the genre pages
    for genre in genre_pages:
        g = Genre.objects.get_or_create(name = genre["name"])[0]
        g.save()

    # Create the game pages
    for game in game_pages:
        g = Game(name = game["name"], desc = game["desc"])
        for genre in game["genres"]:
            g.genres.add(genre)

    # Create the reviews
    for review in reviews:
        pass



# Execution
if __name__ == "__main__":
    print("Populating Hi-Score database...")
    populate()