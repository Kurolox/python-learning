import random
import re


def get_input():
    print("Insert the number of dices you want to roll (format xdY+Z.)")
    while True:
        diceinput = input()
        pattern = re.compile(r"(\d+)(d|D)(\d+)((\+|-)(\d+))?")
        mo = pattern.search(diceinput)
        if mo is not None:
            dicelist = {"nodices": int(mo.group(1)),
                        "dnumber": int(mo.group(3))}
            if mo.group(4) is None:
                dicelist["modifier"] = 0
            else:
                dicelist["modifier"] = int(mo.group(4))
            return dicelist
        else:
            print("That's not a correct input. Try again.")
    #    else:
    #        print("That's not a valid input. Try again.")


def rolling_dices(dicedict):
    actualdiceroll = 0
    totaldiceroll = 0
    print("Rolling " + str(dicedict["nodices"]) +
          " " + str(dicedict["dnumber"]) + "-sided dices with a"
          " modifier of " + str(dicedict["modifier"]) + ".\n")
    for dice in range(dicedict["nodices"]):
        actualdiceroll = random.randint(1, dicedict["dnumber"])
        totaldiceroll += actualdiceroll
        print(actualdiceroll, end=" ")
    print("\n\nTotal without modifier: " + str(totaldiceroll))
    print("Total with modifier: " +
          str(totaldiceroll + dicedict.get("modifier", 0)))


rolling_dices(get_input())
