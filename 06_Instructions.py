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
        print("For circle questions, make sure to round your answer to 2 decimal")
        print("places")
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

# Main Routine...

# Ask if they want instructions
show_instructions = input("Press <enter> for instructions or <any other key> to skip: ")

# If they want instructions, show them
if show_instructions == "":
    instructions()

# Otherwise don't
print("Program continues...")
    
            
