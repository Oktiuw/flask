from shape import Shape

class Triangle(Shape):
    def __init__(self: object, size, pen: str):
        Shape.__init__(self, pen)
        self._size = size
    def _getSize(self):
        return self._size
    @property
    def size(self):
        return self._getSize()
    def draw(self: object) -> None:
        for i in range(self.size):
            print(self.pen*(i+1))
    def _getPerimeter(self: object) -> float:
        return self.size*2+(self.size**2+self.size**2)**0.5
    def _getSurface(self: object) -> float:
        return (self.size*self.size)/2
