def durationToString(minutes: int) -> str:
    return f"{minutes // 60:02}:{minutes % 60:02}"


def ratingToStars(rating, maxi) -> str:
    res = ""
    rating=int(rating)
    for i in range(rating):
        res += "★"
    while len(res) < maxi:
        res += "☆"
    return res


class Movie:
    def __init__(self: object, title: str, duration: int = 0, rating: float = 0.0):
        self._title = title
        self._duration = duration
        if not 0 <= rating <= 10:
            raise ValueError
        self.rating = rating

    # Mise en place de la propriété “title” en lecture seule
    def _getTitle(self: object) -> str:
        return self._title

    @property
    def title(self: object) -> str:
        """
        Retourne le titre du film.
        Retour:
        Titre du film
        """
        return self._getTitle()

    # Mise en place de la propriété “duration” en lecture seule
    def _getDuration(self: object) -> int:
        return self._duration

    @property
    def duration(self: object) -> int:
        """
        Retourne la durée du film (exprimée en minutes).
        Retour:
        Durée du film
        """

        return self._getDuration()

    # Mise en place de la proprité “rating” en lecture et écriture
    def _getRating(self: object) -> float:
        return self._rating

    def _setRating(self: object, rating: float) -> None:
        self._rating = rating

    @property
    def rating(self: object) -> float:
        """
        Retourne la note donnée au film (comprise entre 0 et 10).
        Retour:
        Note du film
        """

        return self._getRating()

    @rating.setter
    def rating(self: object, r: float) -> None:
        """
        Modifie la note du film.
        La note doit être comprise entre 0 et 10
        Paramètre:
        r: nouvelle note du film (entre 0 et 10)
        """
        if not 0 <= r <= 10:
            raise ValueError
        self._setRating(r)

    def __repr__(self: object) -> str:
        return f"{self.title} ({self.duration})\n{ratingToStars(self.rating,10)}"
