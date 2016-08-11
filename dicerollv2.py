import random
import re


def get_input():
    print("Insert the number of dices you want to roll (format xdY+Z.)")
    while True:
        diceinput = input()
        # Finding pattern xdY(+Z) in the input
        pattern = re.compile(r"(\d+)(d|D)(\d+)((\+|-)(\d+))?")
        mo = pattern.search(diceinput)
        # If the input doesn't have any pattern, ask again.
        if mo is not None:
            dicelist = {"nodices": int(mo.group(1)),
                        "dnumber": int(mo.group(3))}
            # If there's no modifier, default to 0
            if mo.group(4) is None:
                dicelist["modifier"] = 0
            else:
                dicelist["modifier"] = int(mo.group(4))
            return dicelist
        else:
            print("That's not a correct input. Try again.")


def rolling_dices(dicedict):
    actualdiceroll = 0
    totaldiceroll = 0
    print("Rolling " + str(dicedict["nodices"]) +
          " " + str(dicedict["dnumber"]) + "-sided dices with a"
          " modifier of " + str(dicedict["modifier"]) + ".\n")
    # Rolling dices! Whew. I guess that this is the only part that matters.
    for dice in range(dicedict["nodices"]):
        actualdiceroll = random.randint(1, dicedict["dnumber"])
        totaldiceroll += actualdiceroll
        print(actualdiceroll, end=" ")
    print("\n\nTotal without modifier: " + str(totaldiceroll))
    print("Total with modifier: " +
          str(totaldiceroll + dicedict.get("modifier", 0)))

# Starting the program. I need to learn methods, man.
rolling_dices(get_input())
