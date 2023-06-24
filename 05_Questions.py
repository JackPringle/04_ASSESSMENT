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

        L_value = int_generator()
        W_value = int_generator()
        
        print()
        print("Rectangle area = L X W")
        print("Rectangle perimeter = L + L + W + W")
        print()
        print("    ---------------")
        print("    |             |")
        print("  W |             |")
        print("    |             |")
        print("    ---------------")
        print("           L")
        print()

        Q1_start = ""

        start_question = ""
        
        Q1_start_list = ["", "xxx"]

        while Q1_start != "xxx" :
            Q1_start = string_checker("Press <enter> for Question 1 (or xxx to quit): ", Q1_start_list, None)

            if Q1_start == "":
                print("START QUESTION ONE")

            elif Q1_start == "xxx":
                print("End game")
                break
            
        print("**********")
        print("Question 1")
        print("**********")
        print()
        print("                ---------------")
        print("                |             |")
        print(f" W = {W_value} |             |")
        print("                |             |")
        print("                ---------------")
        print(f"                  L = {L_value}")
        print()
        print("The area is ___ metres squared")
        input("Area: ")
        
    elif question_type == "triangle":
        print("Start triangle mode")
        
    elif question_type == "circle":
        print("Start circle mode")
        
    elif question_type == "xxx":
        print("You have quit")
        break
