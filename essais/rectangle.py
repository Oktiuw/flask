from shape import Shape


class Rectangle(Shape):
    def __init__(self: object, width: int, height: int, pen: str):
        """
        Constructeur
        Paramètres:
        width: largeur du rectangle
        height: hauteur du rectangle
        pen: motif pour remplir le rectangle
        """
        Shape.__init__(self, pen)  # Appel du constructeur de Shape
        self._width = width
        self._height = height
    def _getWidth(self):
        return self._width
    def _getHeight(self):
        return self._height
    @property
    def width(self):
        return self._getWidth()
    @property
    def height(self):
        return self._getHeight()

    def _getPerimeter(self: object) -> float:
        return (self.width + self.height) * 2
    def _getSurface(self: object) -> float:
        return self.width * self.height
    def draw(self: object) -> None:
        for i in range(self.height):
            res=""
            for j in range(self.width):
                res+=self.pen
            print(res)