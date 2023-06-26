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

            # Check if the response matches the entire item or just the first character
            # of the item (if it's not empty)
            if response == item or (len(item) > 0 and response == item[0]):
                return item

        # If not in valid list, print error
        print(error)
        print()


# Number checker function...
def num_check(question, num_type, low=None, exit_code=None):
    error = "Please enter a number!"

    # Error message when user enters a number less than low
    if low is not None:
        error = f"Please enter an integer more than {low}"

    while True:
        response = input(question).lower()

        try:
            # If user enters exit code, return response
            if response == exit_code:
                return response

            # Set user response to either an integer or float type
            response = num_type(response)

            # If response is less than or equal to low, print error
            if low is not None and response <= low:
                error = f"Please enter a number more than {low}"
                print(error)

            # Otherwise return response
            else:
                return response

        except ValueError:
            print(error)


# List of valid responses
rtc_list = ["rectangle", "triangle", "circle", "xxx"]
question_start_list = ["", "xxx"]

question_type = ""
question_part = ""

quiz_type = ""

while True:
    question_type = string_checker("R / T / C? ",
                                   rtc_list, "Please enter r / t / c")
    if question_type == "rectangle":
        quiz_type = "rectangle"
        print("Start rectangle mode")

    elif question_type == "triangle":
        quiz_type = "triangle"
        print("Start triangle mode")

    elif question_type == "circle":
        quiz_type = "circle"
        print("Start circle mode")

    elif question_type == "xxx":
        print("You have quit")
        break

    # RECTANGLE QUESTIONS...
    if question_type == "rectangle":

        area_question = "The area is ___ metres squared"
        perimeter_question = "The perimeter is ___ metres"





