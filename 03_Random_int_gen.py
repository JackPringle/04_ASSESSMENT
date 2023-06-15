import random


# Random integer generator function...
def int_generator():

    # Return random integer between 1 and 150 (inclusive)
    return random.randint(1, 150)


# Main routine...

# Loop question when <enter> is pressed (for testing purposes)
while True:
    repeat = input("Generate a number between 1 and 150 (inclusive): ")
    response = repeat
    if repeat == "":
        random_int = int_generator()
        print(random_int)
    else:
        break
