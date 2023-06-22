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

question_type = ""

while question_type != "xxx":
    question_type = string_checker("R / T / C? ",
                                   rtc_list, "Please enter r / t / c")
    if question_type == "rectangle":
        print("Start rectangle mode")
    elif question_type == "triangle":
        print("Start triangle mode")
    elif question_type == "circle":
        print("Start circle mode")
