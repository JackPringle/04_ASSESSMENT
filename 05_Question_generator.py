import random
import textwrap


# Question generator function...
def question_gen(question_type):
    while True:
            
        rec_orientation = random.choice(["vertical", "horizontal"])

        # RECTANGLE QUESTIONS
        if question_type == "rectangle":

            W_value = random.randint(1, 150)
            L_value = random.randint(W_value, 150)
            
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
            
            a_value = random.randint(1, 150)
            b_value = random.randint(1, 150)
            c_value = random.randint(1, 150)
            h_value = random.randint(1, 150)
            
        if a_value == c_value and a_value > b_value:
                print()
                print("              /\               ^")
                print("             /  \              |")
                print("            /    \             |")
                print(" a = {}            c = {}      h = {}".format(a_value, c_value, h_value))
                print("          /        \           |")
                print("         /          \          |")
                print("        /____________\         v")
                print("            b = {}".format(b_value))
                print()
                break

        
            

# Main Routine...

while True:
    input(": ")
    question = question_gen("triangle") 


            
        
        
        
