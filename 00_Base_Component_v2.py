import math
import random


# Functions...

# Instructions function...
def instructions():

    # Instructions here
    while True:
        print("-" * 70)
        print()
        print()
        print("          ---- How to play ----")
        print()
        print()
        print("-" * 70)
        print("First, enter the amount of questions you would like to attempt.")
        print("During the quiz, for each question a random shape of your choice")
        print("choice will be genarated.")
        print("Each question / shape has two parts, Part A (find Area), then")
        print("Part B (find Perimeter)")
        print()
        print("Next, enter what shape type you would like to solve for...")
        print("You can choose from Rectnagles // Triangles // circles.")
        print("Formulas for your choosen shape will be provided.")
        print()
        print("Read the question generated, and answer Part A (Area).")
        print("Using the same shape and values, answeer Part B (Perimeter).")
        print()
        print("If you want to quit the quiz, you can do this when its says")
        print("'or press xxx to quit'")
        print()
        print("Once you have quit, or have answer all of your question parts,")
        print("you can see your Quiz Summary.")
        print()
        print("Thats the gist of it!")
        print("GOOD LUCK, AND ENJOY :)")
        print("-" * 70)
        return ""


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
            break


# Question generator function...
def question_gen(question_type):
    # Make sure the answers are accessible and changeable outside the function as well
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

# Define the question variables
quiz_mode = ""
question_part_one = ""
start_part_two = ""
area_question = "The area is ___ metres squared"
perimeter_question = "The perimeter is ___ metres"

# Set question looping variables
rounds_played = 0
rounds_mode = None

# Show quiz heading
print()
print("*" * 70)
print("*" * 70)
print()
print("           ---- WELCOME TO AREA / PERIMETER QUIZ ----")
print()
print("*******************  -- By Jack Pringle --  **************************")
print("*" * 70)
print()
print()

# Ask if they want to see instructions
show_instructions = input("Press <enter> for instructions or <any other key> to skip: ")

# If they want instructions, show them, otherwise don't
if show_instructions == "":
    instructions()

# Ask how many questions they want
print()
print()
rounds = num_check("How many questions? (or <enter> for infinite mode): ", int, 0, exit_code="")
print()
if rounds == "":
    print("You chose infinite mode!")
    print()

# Set Quiz Summary variables
correct_answers = 0
incorrect_answers = 0
show_summary = ""

# If user enters <enter> start infinite mode
if rounds == "":
    rounds_mode = "infinite"
    rounds = 5

# Ask user what shape they would like to solve areas and perimeters for
print("What shape?")
quiz_mode = string_checker("Rectangle // Triangle // Circle? ",
                           rtc_list, "Please enter r / t / c")

# If user chooses rectangles, call formulas function to print rectangle formulas
if quiz_mode == "rectangle":
    formulas("rectangle")
    show_summary = "yes"

# If user chooses triangles, call formulas function to print triangle formulas
elif quiz_mode == "triangle":
    formulas("triangle")
    show_summary = "yes"

# If user chooses circles, call formulas function to print circle formulas
elif quiz_mode == "circle":
    formulas("circle")
    show_summary = "yes"

# If they haven't chosen a shape, dont show them a quiz summary when they quit
elif quiz_mode == "xxx":
    show_summary = "no"

# START QUESTIONS LOOP (rounds)
while True:

    # Calculate rounds played for infinite mode, customise question heading
    if rounds_mode == "infinite":
        heading = f"          QUESTION {rounds_played + 1} (Infinite mode)"
        rounds += 1

    # If mode is not infinite, show rounds played against total rounds, customise question heading
    else:
        heading = f"          QUESTION {rounds_played + 1} OF {rounds}"

    # If user wants to quit, end question loop
    if quiz_mode == "xxx":
        print("You have ended the quiz")
        print("-" * 70)
        print()
        break

    # Ask if they want part one (area), or to quit
    print("-" * 70)
    question_part_one = string_checker(f"Press <enter> for Question {rounds_played + 1} (or xxx to quit): ",
                                       question_start_list, "Please enter a valid response")
    print("-" * 70)

    # If user wants to quit, end question loop
    if question_part_one == "xxx":
        print("You have ended the quiz")
        print("-" * 70)
        print()
        break

    # If they want the first question, format question heading
    elif question_part_one == "":
        print()
        print("*" * 35)
        print("*" * 35)
        print()
        print(heading)
        print()
        print("*" * 35)
        print("*" * 35)
        print()
        print()

        # If they chose rectangles, generate and print a rectangle question 
        if quiz_mode == "rectangle":
            question_gen("rectangle")

        # If they chose triangles, generate and print a triangles question
        elif quiz_mode == "triangle":
            question_gen("triangle")

        # If they chose circles, generate and print a circles question
        elif quiz_mode == "circle":
            question_gen("circle")

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

            # Set guess answer to a rounded string value, so it can be compared against the circles string ANSWER
            user_string_area_answer = f"{guess_answer:.2f}"

            # If users answer is correct, let them see the correct answer message
            if user_string_area_answer == AREA_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif user_string_area_answer != AREA_ANSWER:
                message = "incorrect"

        # If quiz mode is 'r' or 't', compare answers as floats 
        else:

            # If users answer is correct, let them see the correct answer message
            if guess_answer == AREA_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif guess_answer != AREA_ANSWER:
                message = "incorrect"

        # Correct answer message, add one to users correct answers tally
        if message == "correct":
            print("^^^^ Correct ^^^^")
            print("The area was", AREA_ANSWER)
            print()
            print("-" * 70)

            correct_answers += 1

        # Incorrect answer message, add one to users incorrect answers tally
        elif message == "incorrect":
            print("XXXX Incorrect XXXX")
            print("The area was", AREA_ANSWER)
            print()
            print("-" * 70)

            incorrect_answers += 1

    # Ask if they want part 2 (perimeter), or to quit
    question_part_two = string_checker("Press <enter> for Part Two (or xxx to quit): ",
                                       question_start_list, "Please enter a valid response")
    print("-" * 70)

    # If the user wants to quit, end question loop
    if question_part_two == "xxx":
        print("You have ended the quiz")
        print("-" * 70)
        print()
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
        print()

        # Print the perimeter question
        print(perimeter_question)

        # Get user to enter their answer, check answer is valid
        guess_answer = num_check("Perimeter: ", float, 0, "xxx")
        print()

        # Check users perimeter answers...

        # If quiz mode is circle, compare answers as rounded strings (2dp)
        if quiz_mode == "circle":

            # Set guess answer to a rounded string value, so it can be compared against the circles string ANSWER
            user_string_perimeter_answer = f"{guess_answer:.2f}"

            # If users answer is correct, let them see the correct answer message
            if user_string_perimeter_answer == PERIMETER_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif user_string_perimeter_answer != PERIMETER_ANSWER:
                message = "incorrect"

        # If quiz mode is 'r' or 't', compare answers as floats 
        else:

            # If users answer is correct, let them see the correct answer message
            if guess_answer == PERIMETER_ANSWER:
                message = "correct"

            # If users answer is incorrect, let them see the incorrect answer message
            elif guess_answer != PERIMETER_ANSWER:
                message = "incorrect"

        # Correct answer message, add one to users correct answers tally
        if message == "correct":
            print("^^^^ Correct ^^^^")
            print("The perimeter was", PERIMETER_ANSWER)
            print()
            
            correct_answers += 1

        # Incorrect answer message, add one to users incorrect answers tally
        elif message == "incorrect":
            print("XXXX Incorrect XXXX")
            print("The perimeter was", PERIMETER_ANSWER)
            print()

            incorrect_answers += 1

    # End of one question, so add 1 to rounds played
    rounds_played += 1

    # Check if we are out of rounds
    # If out of rounds, end questions loop
    if rounds_played >= rounds:
        print("-" * 70)
        print("All Questions Done!")
        print("-" * 70)
        break


# GAME SUMMARY...

if show_summary == "yes" and rounds_mode != "infinite":

    # Work out the percentage of questions won
    percentage = (correct_answers / (rounds * 2)) * 100

    # Convert it into a float so that it can be checked whether it is >= or < 50
    success_rate = float(f"{percentage:.2f}")

    # Ask user to continue (breaks up the quiz for clarity)
    game_summary = input("Enter <any key> to see your Quiz Summary: ")

    # When they enter a key, print Quiz Summary statements and stats  
    print()
    print("*" * 35)
    print()
    print("      ---- QUIZ SUMMARY ----")
    print()
    print("*" * 35)
    print()
    print(f"You wanted {rounds} {quiz_mode} questions...")
    print("-" * 35)
    print()
    print(f"Total questions completed: {rounds_played}")
    print()
    print("-" * 35)
    print(f"Correct answers: {correct_answers}")
    print(f"Incorrect answers: {incorrect_answers}")
    print("-" * 35)
    print()
    print(f"Success Rate: {success_rate}%")

    # If the success rate is greater than or equal to 50, congratulate them!
    if success_rate >= 50:
        print("Well done!")

    # If it's less than 50%, but grater than 0, give them constructive criticism :)
    elif 50 > success_rate > 0:
        print("Theres room for improvement!")

    # If its zero, yikes!
    elif success_rate == 0:
        print("Yikes!")

# Thank user for playing when quiz ends
print()
print("*" * 70)
print("*" * 70)
print()
print("          ---- ! THANKYOU FOR PLAYING ! ----")
print()
print("*" * 70)
print("*" * 70)
print()

