"""One-shot Wordle."""

__author__ = "730468022" 

wordle: str = "python"
guess: str = input("What is your 6-letter guess?") 

WHITE: str = "\U00002B1C"
GREEN: str = "\U0001F7E9"
YELLOW: str = "\U0001F7E8"

tries: int = 0
index: int = 0
result: str = ""

while tries < 6:
    if len(guess) != 6:
        print("That was not 6 letters! Try again:")
        guess = input()
        tries = tries + 1 
    else:     
        tries = 6
        if guess == wordle:
            result = GREEN + GREEN + GREEN + GREEN + GREEN + GREEN 
            print(result)
            print("Woo! You got it!")
        if guess != wordle:
            while index < len(wordle):
                if guess[index] == wordle[index]:
                    result = result + GREEN
                else:
                    exist: bool = False
                    alternate: int = 0
                    while alternate < len(wordle) and exist is not True: 
                        if guess[index] == wordle[alternate]:
                            exist = True
                            result = result + YELLOW
                        else:
                            alternate = alternate + 1
                    if exist is False:
                        result = result + WHITE    
                index = index + 1
            print(result)    
            print("Not quite. Play again soon!")