"""Dictionary Test."""
__author__ = "730468022"

from exercises.ex06.dictionary import count, favorite_color, invert


def test_invert_one() -> None:
    """Tests for 1 entry only."""
    d = {'apple': 'cat'}
    r = invert(d)
    print(r)
    assert invert(d) == {'cat': 'apple'}
    

def test_invert_three() -> None:
    """Tests for 3 entries."""
    d = {'a': 'z', 'b': 'y', 'c': 'x'}
    r = invert(d)
    print(r)
    assert invert(d) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_many() -> None:
    """Tests for multiple entries."""
    d = {'a': 'b', 'c': 'd', 'e': 'f', 'g': 'h'}
    assert invert(d) == {'b': 'a', 'd': 'c', 'f': 'e', 'h': 'g'}


def test_favorite_color_one() -> None:
    """Tests for one given color."""
    d = {"marx": "yellow"}
    assert favorite_color(d) == "yellow"


def test_favorite_color_three() -> None:
    """Tests for three given colors."""
    d = {"Marx": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(d) == "blue"


def test_favorite_color_tie() -> None:
    """Tests for a tie in color."""
    d = {"Marx": "yellow", "Paul": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(d) == "yellow"


def test_count_one() -> None:
    """Tests for 1 name."""
    names = ["marcus"]
    assert count(names) == {"marcus": 1}


def test_count_three() -> None:
    """Tests for 3 names."""
    names = ["mark", "marcus", "mark"]   
    assert count(names) == {"mark": 2, "marcus": 1}


def test_count_many() -> None:
    """Tests for multiple names."""
    names = ["mark", "marcus", "mark", "mark", "marcus", "skyler", "jackson"]   
    assert count(names) == {"mark": 3, "marcus": 2, "skyler": 1, "jackson": 1}