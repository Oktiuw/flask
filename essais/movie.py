def durationToString(minutes: int) -> str:
    h = str(minutes // 60)
    m = str(minutes % 60)
    if len(h) < 2:
        h = "0" + h
    if len(m) < 2:
        m = "0" + m
    return h+":"+m
