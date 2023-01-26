def durationToString(minutes: int) -> str:
    return f"{minutes // 60:02}:{minutes % 60:02}"


def ratingToStars(rating, maxi) -> str:
    res = ""
    for i in range(rating):
        res += "★"
    while len(res) < maxi:
        res += "☆"
    return res


class Movie:
    def __init__(self, title: str, duration: int, rating=0):
        if rating > 10 or rating < 0:
            raise ValueError
        self.title = title
        self._duration = duration
        self._rating = float(rating)

    def getTitle(self) -> str:
        return self.title

    def getDuration(self) -> int:
        return self._duration

    def getRating(self) -> float:
        return self._rating

    def setRating(self, rating: float):
        if rating > 10 or rating < 0:
            raise ValueError
        self._rating = rating
