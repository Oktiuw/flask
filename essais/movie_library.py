from movie import Movie


class MovieLibrary:
    def __init__(self):
        self._movies = []

    def addMovie(self, film: Movie):
        if self.containsMovieWithTitle(film.title):
            raise ValueError
        self._movies.append(film)

    def containsMovieWithTitle(self, title: str):
        return title in [movie.title for movie in self._movies]

    def getTotalDuration(self):
        return sum([movie.duration for movie in self._movies])

    def showMoviesWithGenre(self,genre):
        return ' '.join([str(movie)+"\n" for movie in self._movies if movie.hasGenre(genre)])
