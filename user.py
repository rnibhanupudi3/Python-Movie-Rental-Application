from movie import Movie
class User:
    def __init__(self, name):
        self.name = name
        self.movies = []
    
    def __repr__(self):
        return f"<User: {self.name}>"
    
    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))
    
    def delete_movie(self,name):
        self.movies = [movie for movie in self.movies if movie.name!=name]
    
    def watched_movies(self):
        return [movie for movie in self.movies if movie.watched]
        #return list(filter(lambda x: x.watched, self.movies))
    
    def save_to_file(self):
        with open(self.name+".txt", "w") as f:
            f.write(self.name + "\n")
            for movie in self.movies:
                f.write(f"{movie.name}, {movie.genre}, {str(movie.watched)}\n")

    def set_watched(self,name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True

    @classmethod            
    def load_from_file(cls, fname):
        with open(fname, "r") as f:
            content = f.readlines()
            username = content[0].strip()
            movies = []
            for line in content[1:]:
                movie_data = line.split(",")
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2]=="True"))

            user = cls(username)
            user.movies = movies
            return user

    def json(self):
        return {"name": self.name, "movies": [movie.json() for movie in self.movies]}

    @classmethod
    def from_json(cls, json_data):
        user = User(json_data["name"])
        movies = [Movie.from_json(movie_data) for movie_data in json_data["movies"]]
        user.movies = movies
        return user