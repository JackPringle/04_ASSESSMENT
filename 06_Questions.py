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


# Main routine...

start_question = False

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
        quiz_type = "rectnagle"
        print("Start rectangle mode")
        break

    elif question_type == "triangle":
        quiz_type = "triangle"
        print("Start triangle mode")
        break
        
    elif question_type == "circle":
        quiz_type = "circle"
        print("Start circle mode")
        break
        
    elif question_type == "xxx":
        print("You have quit")
        break

# RECTANGLE QUESTIONS...
while question_type == "rectangle":

    area_question = "The area is ___ metres squared"
    perimeter_question = "The perimeter is ___ metres"

    print("-" * 70)
    print()
    print("FORMULAS:")
    print()
    print("Rectangle area = L X W")
    print("Rectangle perimeter = 2L + 2W")
    print()
    print("    ---------------")
    print("    |             |")
    print("    |             | W")
    print("    |             |")
    print("    ---------------")
    print("           L")
    print()
    print("-" * 70)

    # Ask the user if they want the next question
    while True:
        Question_start = string_checker("Press <enter> for Question (question number) (or xxx to quit): ", question_start_list, None)

        if Question_start == "":
            start_question = True
            break

        elif Question_start == "xxx":
            print("You chose to end the quiz")
            break

    if start_question == True:
        print()
        print("************")
        print("Question 1")
        print("************")
        print()
        print()
        print("---PART A---")
        print()
        print()
        question_part = "area"

    while True:

        # Generate width first
        W_value = int_generator()

        # Generate a length value that is greater than or equal to width
        # So that length is always the longest side (unless its a square)
        while True:
            L_value = int_generator()
                    
            if L_value >= W_value:
                break
                
        guess_answer = ""
        orientation = random.choice(["vertical", "horizontal"])
                        
        if L_value > W_value:
            if orientation == "vertical":  
                print()
                print("    ----------")
                print("    |        |")
                print("    |        |")
                print(f"    |        | L = {L_value}") 
                print("    |        |")
                print("    |        |")
                print("    |        |")
                print("    ----------")
                print(f"     W = {W_value}")
                print()
            elif orientation == "horizontal":
                print("    ---------------")
                print("    |             |")
                print(f"    |             | W = {W_value}")
                print("    |             |")
                print("    ---------------")
                print(f"        L = {L_value}")
                print()
                        
        if W_value == L_value:
            print()
            print("    ----------")
            print("    |         |")
            print(f"    |         | L = {L_value}")
            print("    |         |")
            print("    |         |")
            print("    ----------")
            print(f"      W = {W_value}")
            print()
                    
        if question_part == "area":

            ANSWER = W_value * L_value
                    
            print(area_question)
            guess_answer = num_check("Area: ", float, 0, "xxx")
            print()

            if guess_answer == "xxx":
                print("You chose to end the quiz")
                break
                    
            if guess_answer == ANSWER:

                question_part = "perimeter"
                        
                print("^ Correct ^")
                print(f"The answer was {ANSWER}")
                print()
                break
                    
            elif guess_answer != ANSWER:

                question_part = "perimeter"
                        
                print(" X Incorrect X")
                print(f"The answer was {ANSWER}")
                print()
                break

        start_question = False

    # Ask the user if they want the next question
    while True:
        Question_start = string_checker("Press <enter> for Question One: Part Two (or xxx to quit): ", question_start_list, None)

        if Question_start == "":
            start_question = True
            break

        elif Question_start == "xxx":
            print("You chose to end the quiz")
            break

    if start_question == True:
        print()
        print()
        print("---PART B---")
        print()
        print()
        question_part = "perimeter"
                          
        if question_part == "perimeter":

            ANSWER = (2 * L_value) + (2 * W_value)
                    
            print(perimeter_question)
            guess_answer = num_check("perimeter: ", float, 0, "xxx")
            print()

            if guess_answer == "xxx":
                print("You chose to end the quiz")
                break

            if guess_answer == ANSWER:

                print("^ Correct ^")
                print(f"The answer was {ANSWER}")
                print()
                break
                    
            elif guess_answer != ANSWER:
                        
                print(" X Incorrect X")
                print(f"The answer was {ANSWER}")
                break

        print("Begin next question... (looping component)")

# TRIANGLE QUESTIONS...
while quiz_type == "triangle":
    print("Write triangle mode here")
    break

# CIRCLE QUESTIONS...
while quiz_type == "circle":
    print("Write circle mode here")
    break
