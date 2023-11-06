#Imports
import time
import threading
import json

from imdb import Cinemagoer
from favorites import add_to_favorites


def loading_animation():
    animation = "|/-\\"
    for _ in range(10):
        for i in range(len(animation)):
            time.sleep(0.1)
            print(f"\rLoading... {animation[i]}", end='', flush=True)
    # Clear the loading animation using backspace and print something else
    print("\r" + " " * len("Loading... ") + "\rDONE! Enjoy your movie :)\n")


def movie_details():
    #Grabs random movie
    movie = input("What movie would you like to search?: ")

    #Generate Instance of IMDb class
    ia = Cinemagoer()

    loading_thread = threading.Thread(target=loading_animation)
    loading_thread.start()

    #Grab's movie id from IMDb
    movie_title = ia.search_movie(f"{movie}")
    id = movie_title[0].movieID

    #Movie from IMDb according to movie ID
    movie_from_IMDb = ia.get_movie(id)

    #Obtain Summary Info
    try:
        summary = movie_from_IMDb['plot'][0]
    except KeyError:
        print("Date not found")

    #Obtain Director Info
    try:
        directors = []
        for director in movie_from_IMDb['directors']:
            directors.append(director['name'])
    except KeyError:
        directors.append('N/A')

    #Obtain Genre and Date
    genre = movie_from_IMDb['genre'][0]
    date = movie_from_IMDb['year']

    actors = []
    for actor in movie_from_IMDb['actors']:
        actors.append(actor['name'])

    loading_thread.join()

    #Print necessary information
    print(f"Movie: {movie_from_IMDb}")
    print(f"Year: {date}")
    print(f"Genre: {genre}")
    print(f"\nDirectors: {', '.join(directors)}")
    print(f"\nActors: {', '.join(actors[:4])}")
    print(f"\nSummary: {summary}")

    #Add movie to favorites
    favorite = input('Would you like to add to favorites?: (y/n)')
    if favorite == 'y':
        add_to_favorites(movie_from_IMDb, date, genre)


if __name__ == '__main__':
    movie_details()