import random
import re


def get_input():
    print("Insert the number of dices you want to roll (format xdY+Z.)")
    diceinput = input()
    pattern = re.compile(r"(\d+)(d|D)(\d+)(\+|-)(\d+)")
    mo = pattern.search(diceinput)
    dicelist = [mo.group(1), mo.group(3), mo.group(4), mo.group(5)]
    return dicelist


def rolling_dices(diceformat):
    actualdiceroll = 0
    totaldiceroll = 0
    print("Rolling " + str(diceformat[0]) +
          " " + str(diceformat[1]) + "-sided dices with a"
          " modifier of " + str(diceformat[2]) + str(diceformat[3]) + ".\n")
    for dice in range(int(diceformat[0])):
        actualdiceroll = random.randint(1, int(diceformat[1]))
        totaldiceroll += actualdiceroll
        print(actualdiceroll, end=" ")
    print("\n\nTotal without modifier: " + str(totaldiceroll))
    print("Total with modifier: " +
          str(int(totaldiceroll + int(str(diceformat[2] + str(diceformat[3]))))))


rolling_dices(get_input())
