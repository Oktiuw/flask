def durationToString(minutes: int) -> str:
    return f"{minutes // 60:02}:{minutes % 60:02}"


def ratingToStars(rating, maxi) -> str:
    res = ""
    for i in range(rating):
        res += "★"
    while len(res) < maxi:
        res += "☆"
    return res
