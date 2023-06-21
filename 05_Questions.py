import random


# Functions...

# Random integer generator function...
def int_generator():
    # Return random integer between 1 and 150 (inclusive)
    return random.randint(1, 150)


# String checker function
def string_checker(question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(question).lower()

        # Check the string is in the valid list
        for item in valid_list:
            if response == item or response == item[0]:
                print("program continues")
                return item

        # If not in valid list, print error
        print(error)
        print()


# Main routine...

# List of valid responses
rtc_list = ["rectangle", "triangle", "circle", "xxx"]


question_type = string_checker("What shape would you like to solve areas AND perimeters for?: ", rtc_list, "Please "
                                                                                                           "enter 'r'"
                                                                                                           " or 't' "
                                                                                                           "or 'c'")
