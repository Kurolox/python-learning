def making_sandwich (bread="Normal", meat="Chicken", *toppings):
    print("We got your order. It's in the oven right now.")
    print ("Preparing your " + bread + " bread...")
    print ("Preparing your " + meat + " meat...")
    print ("Preparing the following toppings:")
    for topping in toppings:
        print ("\n\t- ".join(topping))
    print ("Everything is done! Enjoy your sandwich.")

# Flag for loops because I don't know how to break two times in a row
active_loop = True

# Note to myself: Turn all of this into a function.
# If I need to copy and paste the code, then I can do it with one function.

print ("Hello. What bread do you want? (Default is normal)")
while active_loop == True:  # Loop for keep asking until he decides
    bread_selected = input()
    if bread_selected == "":
        print ("Since you didn't select anything, I'll take normal bread.")
        bread_selected = "normal"
    print ( bread_selected.capitalize() + ", Are you sure? (Y/N)")
    selection = input()
    if selection.lower() == ("y" or "yes"):
        active_loop = False # Get out of the loop
    else:
        print ("Ok. What type of bread do you want then?")  # Repeat the loop

# This one is literally a copypaste of the last one, so i won't comment again.
active_loop = True
print ("What meat do you want? (Default is chicken)")
while active_loop == True:
    meat_selected = input()
    if meat_selected == "":
        print ("Since you didn't select anything, I'll take chicken meat.")
        meat_selected = "chicken"
    print ( meat_selected.capitalize() + ", Are you sure? (Y/N)")
    selection = input()
    if selection.lower() == ("y" or "yes"):
        active_loop = False
    else:
        print ("Ok. What type of meat do you want then?")

# Now for the toppings
active_loop = True
secondary_loop = True
toppings = []

print ("I'll take the order of your toppings right now.")
print ("Just introduce your toppings one at a time. (Q or Quit for stopping)")
while active_loop == True:
    while secondary_loop == True:
        topping_selected = input()
        if topping_selected.lower() == ("q" or "quit"):
            secondary_loop = False
            break
        toppings.append(topping_selected)
    print ("\nHere are all the toppings you ordered:")
    for topping in toppings:
        print ("\t- " + topping)
    print ("Are you okay with that? (Y/N)")
    selection = input()
    if selection.lower() == ("y" or "yes"):
        active_loop = False
    else:
        print ("Ok. We'll take the order of your toppings again. One at a time")
        secondary_loop = True

making_sandwich (bread_selected, meat_selected, toppings)
