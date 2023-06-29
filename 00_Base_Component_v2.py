import math
import random


# Functions...

# String checker function...
def string_checker(string_question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(string_question).lower()

        # Check the string is in the valid list
        for item in valid_list:

            # Check if the response matches the entire item or just the first character
            # of the item (if it's not empty)
            if response == item or (len(item) > 0 and response == item[0]):
                return item

        # If not in valid list, print error
        print(error)
        print()


# Formulas function...
def formulas(formula_type):
    while True:

        # Print rectangle formulas and shape when called
        if formula_type == "rectangle":
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
            break

        # Print triangle formulas and shape when called
        if formula_type == "triangle":
            print("-" * 70)
            print()
            print("FORMULAS:")
            print()
            print("Triangle area = 1/2 X b X h")
            print("Triangle perimeter = a + b + c")
            print()
            print("             /\           ^")
            print("            /  \          |")
            print("           /    \         | h")
            print("        a /      \ c      |")
            print("         /        \       |")
            print("        /__________\      v")
            print("              b ")
            print()
            print("-" * 70)
            break

        # Print circle formulas and shape when called
        if formula_type == "circle":
            print("-" * 70)
            print()
            print("FORMULAS:")
            print()
            print("Circle area = π X r^2")
            print("Circle perimeter = 2π X r ")
            print("π = 3.14159")
            print()
            print("                     _____")
            print("                 --         --")
            print("               --              --")
            print("              ---              ---")
            print("             |             r      |")
            print("            |          o-----------|")
            print("            |                      |")
            print("             |                    |")
            print("              ___              ___")
            print("                __            __")
            print("                  __ ______ __")
            print()
            print("-" * 70)
            break


# Question generator function...
def question_gen(question_type):

    # Make sure the answers are accessable and changable outside the function aswell
    global AREA_ANSWER
    global PERIMETER_ANSWER

    while True:

        # Chose random orientations for rectangles and isosceles
        rec_orientation = random.choice(["vertical", "horizontal"])
        isos_orientation = random.choice(["vertical", "horizontal"])

        # RECTANGLE QUESTIONS
        if question_type == "rectangle":

            # Generate values
            W_value = random.randint(1, 150)
            L_value = random.randint(W_value, 150)

            # Calculate answers
            AREA_ANSWER = L_value * W_value
            PERIMETER_ANSWER = 2 * L_value + 2 * W_value

            # if L is greater than W, generate from two different orientations of rectangles
            if L_value > W_value:
                if rec_orientation == "vertical":

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
                    break

                elif rec_orientation == "horizontal":
                    print("    ---------------")
                    print("    |             |")
                    print(f"    |             | W = {W_value}")
                    print("    |             |")
                    print("    ---------------")
                    print(f"        L = {L_value}")
                    print()
                    break

            # Square shape if all sides are equal
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
                break

        # TRIANGLE QUESTIONS
        if question_type == "triangle":

            # Generate values
            a_value = random.randint(1, 150)
            b_value = random.randint(1, 150)
            c_value = random.randint(1, 150)
            h_value = random.randint(1, 150)

            # Calculate answers
            AREA_ANSWER = 0.5 * b_value * h_value
            PERIMETER_ANSWER = a_value + b_value + c_value

            # print narrow isosceles triangle
            if a_value == c_value and a_value > b_value:
                print()
                print("              /\               ^")
                print("             /  \              |")
                print("            /    \             |")
                print("   a = {}           c = {}      h = {}".format(a_value, c_value, h_value))
                print("          /        \           |")
                print("         /          \          |")
                print("        /            \         | ")
                print("       /______________\        v")
                print("            b = {}".format(b_value))
                print()
                break

            # print flat isosceles triangle
            elif a_value == c_value and a_value < b_value:
                print()
                print("                _/\_                ^")
                print("              _/    \_              |")
                print("            _/        \_            |")
                print("    a = {}                c = {}     h = {}".format(a_value, c_value, h_value))
                print("        _/                \_        |")
                print("      _/                    \_      |")
                print("     /________________________\     v")
                print("            b = {}".format(b_value))
                print()
                break

            # if all sides are equal, print equilateral triangle
            elif a_value == b_value == c_value:
                print()
                print("                              ^")
                print("              /\              |")
                print("             /  \             |")
                print("    a = {}          c = {}     h = {}".format(a_value, c_value, h_value))
                print("           /      \           |")
                print("         /          \         |")
                print("        /            \        | ")
                print("       /______________\       v")
                print("            b = {}".format(b_value))
                print()
                break

            # if all sides are different lengths, print from TWO variations of isosceles triangles
            elif a_value != b_value != c_value:

                # Variation 1
                if isos_orientation == "vertical":
                    print()
                    print("     (side lengths are not proportional)")
                    print()
                    print()
                    print("          \_                     ^")
                    print("           \ \_                  |")
                    print("            \  \                 |")
                    print("      a = {}       c = {}         h = {}".format(a_value, c_value, h_value))
                    print("              \    \_            |")
                    print("               \     \_          |")
                    print("                \      \_        |")
                    print("                 \       \_      |")
                    print("                  \________\     v")
                    print("                    b = {}".format(b_value))
                    print()
                    break

                # Variation 2
                if isos_orientation == "horizontal":
                    print()
                    print("     (side lengths are not proportional)")
                    print()
                    print()
                    print("                /\ _                     ^")
                    print("               /     \ _                 |")
                    print("       a = {}              c = {}         h = {}".format(a_value, c_value, h_value))
                    print("             /               \ _         |")
                    print("            /____________________\       v")
                    print("                  b = {}".format(b_value))
                    print()
                    break

        # CIRCLE QUESTIONS
        if question_type == "circle":

            # Generate values
            r_value = random.randint(1, 150)

            # Calculate answers
            unrounded_area = math.pi * (r_value ** 2)
            unrounded_perimeter = 2 * math.pi * r_value
            AREA_ANSWER = f"{unrounded_area:.2f}"
            PERIMETER_ANSWER = f"{unrounded_perimeter:.2f}"

            # Unique diameter question
            if r_value >= 75:
                print()
                print("                     _____")
                print("                 --         --")
                print("               --              --")
                print("              ---              ---")
                print("             |            d = {}    ".format(r_value * 2))
                print("            |----------o-----------|")
                print("            |                      |")
                print("             |                    |")
                print("              ___              ___")
                print("                __            __")
                print("                  __ ______ __")
                print()
                break

            # Small circle
            if r_value < 75:
                print()
                print("               ___")
                print("            --     --")
                print("          |           |")
                print("         |      .______|")
                print("         |      r = {}   ".format(r_value))
                print("          |           |")
                print("            -- ___ --")
                print()
                break

# Number checker function...
def num_check(num_question, num_type, low=None, exit_code=None):
    error = "Please enter a number!"

    # Error message when user enters a number less than low
    if low is not None:
        error = f"Please enter an integer more than {low}"

    # Input the question, allow lowercase and uppercase
    while True:
        response = input(num_question).lower()

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

        # If user enters an incorrect value, print the error message
        except ValueError:
            print(error)


# Main Routine...

# List of valid responses for quiz mode question and next question part question
rtc_list = ["rectangle", "triangle", "circle", "xxx"]
question_start_list = ["", "xxx"]

# Define variables
quiz_mode = ""
question_part_one = ""
start_part_two = ""
area_question = "The area is ___ metres squared"
perimeter_question = "The perimeter is ___ metres"

# Start question loop
end_quiz = "no"
while end_quiz == "no":

    rounds_played = 0
    mode = None

    # Ask user what shape they would like to solve areas and perimeters for
    print("What shape?")
    quiz_mode = string_checker("Rectangle // Triangle // Circle? ",
                               rtc_list, "Please enter r / t / c")

    # If user wants to quit, end question loop
    if quiz_mode == "xxx":
        print("You have ended the quiz")
        break

    # If user chooses rectangles, call formulas function to print rectangle formulas
    if quiz_mode == "rectangle":
        formulas("rectangle")

    # If user chooses triangles, call formulas function to print triangle formulas
    elif quiz_mode == "triangle":
        formulas("triangle")

    # If user chooses circles, call formulas function to print circle formulas
    elif quiz_mode == "circle":
        formulas("circle")

    # Ask if they want part one (area), or to quit
    question_part_one = string_checker("Press <enter> for Question _ (or xxx to quit): ",
                                       question_start_list, "Please enter a valid response")
    print("-" * 70)

    # If user wants to quit, end question loop
    if question_part_one == "xxx":
        print("You have ended the quiz")
        break

    # If they want the first question, format question heading
    elif question_part_one == "":
        print()
        print("*" * 35)
        print("*" * 35)
        print()
        print("          QUESTION _ OF _")
        print()
        print("*" * 35)
        print("*" * 35)
        print()
        print()

        # If they chose rectangles, generate and print a rectangle question 
        if quiz_mode == "rectangle":
            question = question_gen("rectangle")

        # If they chose triangles, generate and print a triangles question
        elif quiz_mode == "triangle":
            question = question_gen("triangle")

        # If they chose circles, generate and print a circles question
        elif quiz_mode == "circle":
            question = question_gen("circle")

        # Print Part A heading
        print()
        print("-" * 70)
        print()
        print(" ---PART A---")
        print()
        print()

        # Print the area question
        print(area_question)

        # Get user to enter their answer, check answer is valid
        guess_answer = num_check("Area: ", float, 0, "xxx")
        print()

        # Check users area answers...

        # If quiz mode is circle, compare answers as rounded strings (2dp)
        if quiz_mode == "circle":

            # Set guess answer to a rounded string value so it can be compared against the circles string ANSWER
            user_string_area_answer = f"{guess_answer:.2f}"
            
            # If users answer is corect, let them see the correct answer message
            if user_string_area_answer == AREA_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif user_string_area_answer != AREA_ANSWER:
                message = "incorrect"

        # If quiz mode is 'r' or 't', compare answers as floats 
        else:
            
            # If users answer is corect, let them see the correct answer message
            if guess_answer == AREA_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif guess_answer != AREA_ANSWER:
                message = "incorrect"

        # Correct answer message
        if message == "correct":
            print("^^^^ Correct ^^^^")
            print("The area was", AREA_ANSWER)
            print()
            print("-" * 70)

        # Incorrect answer message
        elif message == "incorrect":
            print("XXXX Incorrect XXXX")
            print("The area was", AREA_ANSWER)
            print()
            print("-" * 70)
            
                
    # Ask if they want part 2 (perimeter), or to quit
    question_part_two = string_checker("Press <enter> for Part Two (or xxx to quit): ",
                                       question_start_list, "Please enter a valid response")

    # If the user wants to quit, end question loop
    if question_part_two == "xxx":
        print("You have ended the quiz")
        break

    # If they want part 2, format part 2 heading
    elif question_part_two == "":
        print("-" * 70)
        print()
        print(" ---PART B---")
        print()
        print()
        print("Using the same shape from above...")
        print()

        # Print the perimeter question
        print(perimeter_question)

        # Get user to enter their answer, check answer is valid
        guess_answer = num_check("Perimeter: ", float, 0, "xxx")
        print()

        # Check users perimeter answers...

        # If quiz mode is circle, compare answers as rounded strings (2dp)
        if quiz_mode == "circle":

            # Set guess answer to a rounded string value so it can be compared against the circles string ANSWER
            user_string_perimeter_answer = f"{guess_answer:.2f}"
            
            # If users answer is corect, let them see the correct answer message
            if user_string_perimeter_answer == PERIMETER_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif user_string_perimeter_answer != PERIMETER_ANSWER:
                message = "incorrect"

        # If quiz mode is 'r' or 't', compare answers as floats 
        else:
            
            # If users answer is corect, let them see the correct answer message
            if guess_answer == PERIMETER_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif guess_answer != PERIMETER_ANSWER:
                message = "incorrect"

        # Correct answer message
        if message == "correct":
            print("^^^^ Correct ^^^^")
            print("The perimeter was", PERIMETER_ANSWER)
            print()

        # Incorrect answer message
        elif message == "incorrect":
            print("XXXX Incorrect XXXX")
            print("The perimeter was", PERIMETER_ANSWER)

    break

print()
print("END OF CODE")

        
