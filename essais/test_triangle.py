from triangle import Triangle
T:Triangle = Triangle(3, '*')
print("Instanciation avec initialisation :", vars(T))
T.draw()
print(T.perimeter)
print(T.surface)