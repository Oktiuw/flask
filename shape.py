# essais/shape.py
class Shape:
    def __init__(self):
        self._pen=""

    def draw(self: object) -> None:
     pass
    # Préparation de la propriété "perimeter"
    def _getPerimeter(self: object) -> float:
        pass
    @property
    def perimeter(self: object) -> float:
        return self._getPerimeter()
    # Préparation de la propriété "surface"
    def _getSurface(self: object) -> float:
        pass
    @property
    def surface(self: object) -> float:
        return self._getSurface()
    def _getPen(self:object) -> str:
        return self._pen
    def _setPen(self,value:str):
        self._pen=value