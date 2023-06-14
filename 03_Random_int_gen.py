import random


# Random integer generator function...
def int_generator():

    # Return random integer between 1 and 150 (inclusive)
    return random.randint(1, 150)


# Main routine...

# Loop question when <enter> is pressed (for testing purposes)
while True:
    repeat = input("")
    response = repeat
    if repeat == "":
        random_int = int_generator()
        question = f"The length is {random_int}"
        print(question)
        print()
    else:
        break
