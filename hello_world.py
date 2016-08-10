food = ["Sandwich", "Kebab", "Pizza", "pizza", "PiZzA"]
food_Ready = []
while food:
    food_In_Progress = food.pop()
    if food_In_Progress.lower() == "pizza":
        print ("We ran out of Pizza. Deleting all pizza orders.")
        # List normalizer. Just changes every string to lower case.
        for pizza in food:
            pizza = pizza.capitalize
        while "Pizza" in food:
            food.remove("Pizza")
    else:
        print ("I'm preparing your " + food_In_Progress.lower() + ". Please wait.")
        food_Ready.append(food_In_Progress)
print ("\nEverything is done. Here's the full list.\n-------------------------")
for x in food_Ready:
    print (x)
