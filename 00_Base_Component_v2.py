import random


# Functions...

# String checker function...
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
    while True:

        # Chose random orientations for rectangles and isosceles
        rec_orientation = random.choice(["vertical", "horizontal"])
        isos_orientation = random.choice(["vertical", "horizontal"])

        # Create a dictionary of values
        values_dict = {}

        # RECTANGLE QUESTIONS
        if question_type == "rectangle":

            # Generate values
            W_value = random.randint(1, 150)
            L_value = random.randint(W_value, 150)

            # Calculate answers
            AREA_ANSWER = L_value * W_value
            PERIMETER_ANSWER = 2 * L_value + 2 * W_value

            # Update values in the dictionary
            values_dict["L_value"] = L_value
            values_dict["W_value"] = W_value

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

            # Update values in the dictionary
            values_dict["a_value"] = a_value
            values_dict["b_value"] = b_value
            values_dict["c_value"] = c_value
            values_dict["h_value"] = h_value

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
            AREA_ANSWER = 3.14159265358979323846264338327950 * (r_value ** 2)
            PERIMETER_ANSWER = 2 * 3.14159265358979323846264338327950 * r_value

            # Format the answers to two decimal places
            formatted_area = "{:.2f}".format(AREA_ANSWER)
            formatted_perimeter = "{:.2f}".format(PERIMETER_ANSWER)
            AREA_ANSWER = formatted_area
            PERIMETER_ANSWER = formatted_perimeter

            # Update values in the dictionary
            values_dict["r_value"] = r_value

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

    # Set area and perimeter answers to value dictionary, then return the values dictionary
    values_dict["AREA_ANSWER"] = AREA_ANSWER
    values_dict["PERIMETER_ANSWER"] = PERIMETER_ANSWER
    return values_dict


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

# Start one question loop
while True:

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

        # If the user wants to quit, end question loop
        if guess_answer == "xxx":
            print("You have ended the quiz")
            break

        # If the users answer is correct, tell them, then print the answer
        elif guess_answer == question["AREA_ANSWER"]:
            print("^^^^ Correct ^^^^")
            print("The area was", question["AREA_ANSWER"])
            print()

        # If the users answer is incorrect, tell them, then print the answer
        elif guess_answer != question["AREA_ANSWER"]:
            print("XXXXX Incorrect XXXX")
            print(f"The area was", question["AREA_ANSWER"])
            print()
            print("-" * 70)
            
    # Ask if they want part 2 (perimeter), or to quit
    question_part_two = string_checker("Press <enter> for Part Two (or xxx to quit): ",
                                        question_start_list, None)

    # If the user wants to quit, end question loop
    if question_part_two == "xxx":
        print("You have ended the quiz")
        break

    # If they want part 2, format part 2 heading
    elif question_part_two == "":
        print()
        print("-" * 70)
        print()
        print(" ---PART B---")
        print()
        print()
        print("Using the same shape from above...")
        print()

        # Print the perimeter question
        print(perimeter_question)

        # Get the user to enter their answer, check answer is valid
        guess_answer = num_check("Perimeter: ", float, 0, "xxx")
        print()

        # If the user wants to quit, end question loop
        if guess_answer == "xxx":
            print("you have ended the quiz")
            break
        # If the answer is correct, tell them, then print the answer
        elif guess_answer == question["PERIMETER_ANSWER"]:
            print("^^^^ Correct ^^^^")
            print("The perimeter was", question["PERIMETER_ANSWER"])
            print()

        # If the answer is incorrect, tell them, then print the answer
        elif guess_answer != question["PERIMETER_ANSWER"]:
            print("XXXXX Incorrect XXXX")
            print(f"The perimeter was", question["PERIMETER_ANSWER"])
            print()
            print("-" * 70)

            print("END OF CODE")

        break 
