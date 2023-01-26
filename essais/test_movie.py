from movie import durationToString, ratingToStars, Movie

print(durationToString(512))
print(durationToString(4096))
print(durationToString(32768))

print(ratingToStars(0, 8))
print(ratingToStars(2, 8))
print(ratingToStars(4, 8))
print(ratingToStars(8, 8))

m1 = Movie('Les évadés', 140)
print(vars(m1))
print(dir(m1))

try:
    m2: Movie = Movie('Les évadés', 122, 5.5)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')
try:
    m2 = Movie('Les évadés', 122, -0.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")

try:
    m2 = Movie('Les évadés', 122, 10.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")


print(m1.getRating())
print(m1.getDuration())
print(m1.getTitle())


try:
    m2: Movie = Movie('Les évadés', 122, 5.5)
    m2.setRating(4)
    print(m2.getRating())
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')
try:
    m2.setRating(-1)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")
