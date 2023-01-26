from movie import Movie
from movie_library import MovieLibrary

print(Movie.durationToString(512))
print(Movie.durationToString(4096))
print(Movie.durationToString(32768))

print(Movie.ratingToStars(0, 8))
print(Movie.ratingToStars(2, 8))
print(Movie.ratingToStars(4, 8))
print(Movie.ratingToStars(8, 8))

m1 = Movie('Les évadés', ["Drame"], 140)
print(vars(m1))
print(dir(m1))

try:
    m2: Movie = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, 5.5)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')
try:
    m2 = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, -0.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

try:
    m2 = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, 10.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

print(m1.rating)
print(m1.duration)
print(m1.title)

try:
    m2: Movie = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, 5.5)
    m2.rating = 4
    print(m2.rating)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')
try:
    m2.rating = -1
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

m1 = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, 9.0)
print(m1)
# La méthode __repr__ dit comment la classe doit se comporter quand elle est appelée en str


print(m1.hasGenre('Animation'))
print(m1.hasGenre('A'))

m1: Movie = Movie('Les évadés', ["Drame"], 142, 9.0)
m2: Movie = Movie("Les indestructibles", ["Animation", "Action", "Aventure"], 115, 8.0)
m3: Movie = Movie("Le parrain", ["Drame", "Crime"], 177, 7.0)
m4: Movie = Movie("La Liste de Schnidler", ["Drame", "Histoire", "Guerre"], 195, 6.0)
m5: Movie = Movie("La Ligne verte", ["Fantastique", "Drame", "Crime"], 189, 9.0)
m6: Movie = Movie("Your Name", ["Romance", "Animation", "Drame"], 107, 9.0)

movieLib = MovieLibrary()
movieLib.addMovie(m1)
movieLib.addMovie(m2)
movieLib.addMovie(m3)
movieLib.addMovie(m4)
movieLib.addMovie(m5)
movieLib.addMovie(m6)
print(movieLib.containsMovieWithTitle("Les évadés"))
print(movieLib.containsMovieWithTitle("Les bronzés 3"))

try:
    movieLib.addMovie(m1)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

print(movieLib.getTotalDuration())
print(movieLib.showMoviesWithGenre("Drame"))