"""Challenge Question 1."""

choice: int = int(input(" Enter a number: "))

if choice <= 25:
    print("A")
if choice > 25 and choice <= 50:
    print ("B")
if choice > 75:
    print ("C")
if choice > 50 and choice <= 75:
    print ("D")