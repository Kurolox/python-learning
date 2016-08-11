import sys
import os


def show_help():
    print("\thelp: Display this message.")
    print("\texit: Exit the program.")
    print("\tlist: Display the list from the file.")
    print("\tadd: Add an element to the list.")
    print("\tdelete: Remove the list.")


def exit_program():
    print("Exiting. Have a nice day.")
    sys.exit()


def add_to_list():
    print("Please select the file you want to add an element. If the selected file doesn't exist it will be created. Files must be in the working directory.")
    print("\nDetected files: " + ", ".join(os.listdir()))
    selected_file = input()
    if selected_file in os.listdir():
        openfile = open(selected_file, "a")
    else:
        print("I couldn't find any file with that name. I'm creating one for you.")
        openfile = open(selected_file, "w")
    print("Now please input what do you want to add to the list.")
    new_element = input()
    openfile.write("* " + str(new_element) + "\n")
    openfile.close()
    print("Element added!")


def list_list():
    print("Please select the file you want to read. Files must be in the working directory.")
    print("\nDetected files: " + ", ".join(os.listdir()))
    selected_file = input()
    if selected_file in os.listdir():
        openfile = open(selected_file)
        print(openfile.read())
        openfile.close()
    else:
        print("I couldn't find any file with that name.")


def remove_list():
    print("Please select the file you want to delete. Files must be in the working directory.")
    print("\nDetected files: " + ", ".join(os.listdir()))
    selected_file = input()
    if selected_file in os.listdir():
        print("You will remove the file " + selected_file + ". Are you sure? (y/n)")
        confirm = input()
        if ["y", "yes"] in confirm.lower():
            os.remove(selected_file)
        else:
            print("Aborting.")
    else:
        print("I couldn't find any file with that name.")

def get_input():
    print("Todo: To-do list generator. Use \"help\" to see the commands.")
    while True:
        user_command = input()
        if user_command.lower() == "help":
            show_help()
        elif user_command.lower() == "exit":
            exit_program()
        elif user_command.lower() == "add":
            add_to_list()
        elif user_command.lower() == "list":
            list_list()
        elif user_command.lower() == "delete":
            remove_list()
        else:
            print("That's not a valid command. Please try again.")


get_input()
