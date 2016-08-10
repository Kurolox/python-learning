def collatz(number):
    if (number % 2) == 0:
        return number // 2
    else:
        return (3 * number) + 1


def get_input():
    print("Welcome to this Collatz sequence generator. Please input a number.")
    print("I'll show you the full Collazt sequence for said number.")
    while True:
        try:
            return int(input())
        except ValueError:
            print("That's not even a number.")
            continue


number = get_input()
while number is not 1:
    number = collatz(number)
    print(number)
