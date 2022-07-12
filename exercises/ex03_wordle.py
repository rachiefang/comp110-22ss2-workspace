"""Structured Wordle."""
__author__ = "730468022"


def contains_char(word: str, char: str) -> bool:
    """Returns True or False for containing the character."""
    assert len(char) == 1
    index: int = 0
    contains: bool = False
    while index < len(word):
        if word[index] == char:
            return True
        else:
            index = index + 1
    if contains is False:
        return False


def emojified(guess: str, secret: str) -> str: 
    """Returns emoji."""
    WHITE: str = "\U00002B1C"
    GREEN: str = "\U0001F7E9"
    YELLOW: str = "\U0001F7E8"
    result: str = ""
    index: int = 0
    assert len(guess) == len(secret)
    while index < len(secret):
        if contains_char(guess, secret[index]) is True:
            while index < len(secret):
                if guess[index] == secret[index]:
                    result = result + GREEN
                else:
                    exist: bool = False
                    alternate: int = 0
                    while alternate < len(secret) and exist is not True: 
                        if guess[index] == secret[alternate]:
                            exist = True
                            result = result + YELLOW
                        else:
                            alternate = alternate + 1
            index = index + 1
            result = result + YELLOW
            return result
        else: 
            result = result + WHITE
            return result


def input_guess(expected_len: int) -> str:
    """Return incorrect input."""
    guess: str = input(f"Enter a {expected_len} character word:")
    if len(guess) != expected_len:
        return str(f"That wasn't {expected_len} letters! Try again:")
    else:
        return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    turn: int = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(5) 
        secret: str = "codes"
        print(emojified(guess, secret))
        turn = turn + 1
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")   


if __name__ == "__main__":
    main()