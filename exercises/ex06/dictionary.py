"""EX06 Dictionary."""
__author__ = "730468022"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Invert order of key and value."""
    result = dict[str, str]()
    for key, value in d.items():
        result[value] = key
    return result
    print(result)


def favorite_color(d: dict[str, str]) -> str:
    """Return the most favorite color."""
    count = dict[str, int]()
    for student, color in d.items():
        count.setdefault(color, 0)
        count[color] = count[color] + 1
    max_times = 0
    name = ""
    for color, times in count.items():
        if times > max_times:
            max_times = times
            name = color
    return name        


def count(names: list[str]) -> dict[str, int]:
    """Return count."""
    c = dict[str, int]()
    for s in names:
        c.setdefault(s, 0)
        c[s] = c[s] + 1
    return c