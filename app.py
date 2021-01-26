
from user import User
import json
import os

def menu():
    name = input("Enter name: ")
    fname = f"{name}.txt"
    if file_exists(fname):
        with open(fname, "r") as f:
            json_data = json.load(f)
        user = User.from_json(json_data)
    else:
        user = User(name)
        
    user_input = input("Enter 'a' to add movie, 's' to see list of movies, " +
    "'w' to set a movie as watched, 'd' to delete a movie, " +
    "'l' to see list of watched movies, 'f' to save the file and 'q' to quit\n")
    while user_input != "q":
        if user_input == "a":
            movie_name = input("Enter name of movie: ")
            movie_genre = input("Enter genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == "s":
            for movie in user.movies:
                print(f"Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}")
        elif user_input == "w":
            movie_name = input("Enter name of movie: ")
            user.set_watched(movie_name)
        elif user_input == "d":
            movie_name = input("Enter name of movie: ")
            user.delete_movie(movie_name)
        elif user_input == "l":
            for movie in user.watched_movies():
                print(f"Name: {movie.name} Genre: {movie.genre} Watched: {movie.watched}")
        elif user_input == "f":
            with open(fname, "w") as f:
                json.dump(user.json(),f)
        user_input = input("Enter 'a' to add movie, 's' to see list of movies, " +
    "'w' to set a movie as watched, 'd' to delete a movie, " +
    "'l' to see list of watched movies, 'f' to save the file and 'q' to quit\n")


def file_exists(fname):
    return os.path.isfile(fname)

menu()
""" my_movie = Movie("The Matrix", "Action", True)
user1 = User("Rohith")
user1.movies.append(my_movie)
print(user1, user1.movies)
print(user1.watched_movies())

user2 = User("Rohith")
user2.add_movie("The Matrix", "Action")
user2.add_movie("Brug City", "Pog Champ")
user2.save_to_file()

user3 = User.load_from_file("Rohith.txt")
print(user3, user3.movies)

user4 = User("Rohith")
user4.add_movie("The Matrix 2", "Action")
user4.add_movie("Brug City 2", "Pog Champ")
print(user4.json())

with open("my_file.txt", "w") as f:
    json.dump(user4.json(), f)

with open("my_file.txt", "r") as f:
    json_data = json.load(f)
    user = User.from_json(json_data)
    print(user.json()) """
