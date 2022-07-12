"""Choose your own adventure."""
__author__ = "730468022"


player: str = "y/n"
points: int = 0
BREAD: str = "\U0001F35E"
FISH: str = "\U0001F9AD"
ROCKS: str = "\U0001FAA8"


def greet() -> None:
    """Greets player."""
    global player
    player = input("Hello there! What is your name?")
    print(f"Nice to meet you {player}!")
    print("You have a project due tomorrow on the Sumerian trade system.")
    print("You procrastinated but luckily stumbled upon a time machine.")
    print("You cannot get back to the current time period until 72 hours after your arrival.")
    print("You have landed in 4000 BC Sumeria, the birthplace of numbers.")
    print("You visit the marketplace to study how numbers were used in trade. Your stomach grumbles.")
    print("Your goal is to find food before you starve.")


def bread() -> None:
    """If the player chooses bread."""
    global points 
    points = points + 5
    print(f"Baker: Welcome to the {BREAD} stand.")
    print(f"{player}: I do not have any money.")
    print("Baker: Let's play a game. If you can guess how many silver nuggets this piece of bread is, it is yours.")
    print("You have 5 tries.")
    
    tries: int = 1
    from random import randint
    answer: int = randint(1, 10)
    while tries < 6:    
        guess: int = input(f"Pick a number from 1-10. What is your {tries} guess?")
        if guess == answer: 
            points = points + 1
            print("Congratulations! The bread is yours! You have fed yourself and will not starve in Sumeria.")
            print("After 72 hours you may return home with your new gained knowledge of Sumeria.")
            print(f"You earned {points} points.")
            exit()
        if guess != answer:
            print("Try again.") 
            points = points - 1
            tries = tries + 1
            print(f"You have {6 - tries} tries left.")
    if tries == 6:
        print("You were unable to obtain food and starved in Ancient Sumeria.")
        print(f"You earned {points} points. Game over.")
        exit()


def fish() -> None:
    """If the player chooses fish."""
    global points
    points = points + 5
    print(f"Fisherman: Welcome to the {FISH} stand.")
    print(f"{player}: I do not have any money.")
    print("Fisherman: Let's play a game. If you can guess how many silver nuggets this fish is, it is yours.")
    print("You have 5 tries.")
    
    tries: int = 1
    from random import randint
    answer: int = randint(1, 10)
    while tries < 6:    
        guess: int = input(f"Pick a number from 1-10. What is your {tries} guess?")
        if guess == answer: 
            points = points + 1
            print("Congratulations! The fish is yours! You have fed yourself and will not starve in Sumeria.")
            print("After 72 hours you may return home with your new gained knowledge of Sumeria.")
            print(f"You earned {points} points.")
            exit()
        if guess != answer:
            print("Try again.") 
            points = points - 1
            tries = tries + 1
            print(f"You have {6 - tries} tries left.")
    if tries == 6:
        print("You were unable to obtain food and starved in Ancient Sumeria.")
        print(f"You earned {points} points. Game over.")
        exit()


def rocks() -> None:
    """If the player chooses rocks."""
    global points
    points = points + 1
    print(f"Sadly you cannot eat rocks {ROCKS}. You end up starving in ancient Sumeria. Goodbye.")
    print(f"You earned {points} points. Game over.")
    exit()


def main() -> None:
    """The entrypoint of the game."""
    print(greet()) 
    choice: str = input("The marketplace sells bread, fish, and rocks. Which stand will you visit?")
    if choice == "bread":
        print(bread())
    if choice == "fish":
        print(fish())
    if choice == "rocks":
        print(rocks())
    

if __name__ == "__main__":
    main()