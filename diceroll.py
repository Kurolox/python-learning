import random


def get_input():
    diceinput = {"number of dices": 0, "dice number": 0, "modifier": 0}
    print("Hello mate. Welcome to Kurolox dice roller.\n")
    print("Insert the number of dices you want to roll.")
    while True:
        try:
            diceinput["number of dices"] = int(input())
            break
        except ValueError:
            print("That's not a valid input. Try again.")
    print("Insert the dice number of sides.")
    while True:
        try:
            diceinput["dice number"] = int(input())
            break
        except ValueError:
            print("That's not a valid input. Try again.")
    print("Insert a modifier (instert 0 if there's none.)")
    while True:
        try:
            diceinput["modifier"] = int(input())
            break
        except ValueError:
            print("That's not a valid input. Try again.")
    return diceinput


def rolling_dices(dicedict):
    actualdiceroll = 0
    totaldiceroll = 0
    print("Rolling " + str(dicedict.get("number of dices")) +
          " " + str(dicedict.get("dice number")) + "-sided dices with a"
          " modifier of " + str(dicedict.get("modifier")) + ".\n")
    for dice in range(dicedict.get("number of dices")):
        actualdiceroll = random.randint(1, dicedict.get("dice number"))
        totaldiceroll += actualdiceroll
        print(actualdiceroll, end=" ")
    print("\n\nTotal without modifier: " + str(totaldiceroll))
    print("Total with modifier: " +
          str(int(totaldiceroll + dicedict.get("modifier"))))


rolling_dices(get_input())
