# Formula function

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
            print("             |             r     |")
            print("            |          o----------|")
            print("            |                     |")
            print("             |                   |")
            print("              ___              ___")
            print("                __            __")
            print("                  __ ______ __")
            print()                     
            print("-" * 70)
            break


# Main Routine...

# print formulas for testing...
formulas("rectangle")

input(": ")

formulas("triangle")

input(": ")

formulas("circle")
