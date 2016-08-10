"""Fuck docstrings"""
# Dictionary where I store all the poll values
poll = {}
print("Hello. Would you like to take a poll? Say No to finish.")
while True:
    user_input = input()
    # Checking if the user wants to take the poll
    if user_input.lower().strip() != "no":
        # Asking and fetching the name
        print("Thanks for taking the poll. What's your name? ")
        user_name = input()
        # Asking and fetching the color
        print("Ok, " + user_name.capitalize() + ". What's your favourite color?")
        user_color = input()
        print(user_color.capitalize() + ", interesting. Thanks for taking the poll.")
        # Storing the name and the color in to the poll
        poll[user_name.capitalize()] = user_color.capitalize()
        print("\nWould you like to let someone else to take the pool?")
        print("Say 'No' to end the poll and check the results.")
    # User don't want to take the poll. Exiting the loop
    else:
        break
# Showing results
print("\n")  # I could've put this in the next one, but it looks better
print("|-----------------------------|")
print("|          Poll               |")
print("|           Results           |")
print("|-----------------------------|")
for name, color in poll.items():
    print(name.capitalize() + " prefers the color " + color.capitalize + ".")
print("\nThanks for doing the poll!")
