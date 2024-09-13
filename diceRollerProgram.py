# Dice Roller Program

import random

# Dice roller characters from unicode
# unicodeBoxDrawing = print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ●  ┌ ─ ┐ │ └ ┘


diceArt = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"), 
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│      ●  │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│ ●     ● │", 
        "│         │", 
        "│ ●     ● │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│ ●     ● │", 
        "│    ●    │", 
        "│ ●     ● │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "│ ●     ● │", 
        "└─────────┘")                 
}

total = 0
rollAgain = True

while rollAgain:
    dice = []
    numOfDice = int(input("How many dice🎲?: "))

    for die in range(numOfDice):
        dice.append(random.randint(1, 6))
    print()

    # Vertical arrangement of dice charachter
    print("--Vertical Arrangement--")
    for die in range(numOfDice):
        for line in diceArt.get(dice[die]):
            print(line)
    print()
    # for Horizontal arrangement of dice character
    print("--Horizontal Arrangement--")
    for line in range(5):
        for die in dice:
            print(diceArt.get(die)[line], end=" ")
        print()
    for die in dice:
        total += die
    print(f"total: {total}👍")

    if not input("Roll again? (yes or no): ").lower() == "yes":
        rollAgain = False

        print("Thank you for playing!🙏")