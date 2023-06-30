import random
import math


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

# Main Routine...

# Call questions function for testing purposes, all three types, and display answers

while True:
    input("Enter for rectangle: ")
    question = question_gen("rectangle")
    print("The area is", AREA_ANSWER)
    print("The perimeter is", PERIMETER_ANSWER)
    print()

    input("Enter for triangle: ")
    question = question_gen("triangle")
    print("The area is", AREA_ANSWER)
    print("The perimeter is", PERIMETER_ANSWER)
    print()

    input("Enter for circle: ")
    question = question_gen("circle")
    print("The area is (rounded)", AREA_ANSWER)
    print("The perimeter is (rounded)", PERIMETER_ANSWER)
    print()
