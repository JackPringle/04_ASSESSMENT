# Functions...
def num_check(question, num_type, low=None, exit_code=None):
    error = "Please enter a number!"

    # Error message when user enters a number less than low
    if low is not None:
        error = f"Please enter an integer more than {low}"

    while True:
        response = input(question).lower()

        try:
            # Set user response to either an integer or float type
            response = num_type(response)

            # If user enters exit code, return response
            if response == exit_code:
                return response

            # If response is less than or equal to low, print error
            elif low is not None and response <= low:
                error = "Please enter a number more than 0"
                print(error)

            # Otherwise return response
            else:
                return response

        except ValueError:
            print(error)


# Main routine...

rounds_played = 0
rounds = num_check("How many rounds?: ", int, exit_code="xxx")

mode = None

if rounds == "":
    mode = "infinite"
    rounds = 5

# Rounds loop
end_game = "no"
while end_game == "no":

    if mode == "infinite":
        heading = f"Round {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Start Round!!
    while True:

        print("**Question goes here**")
        print()
        guess = num_check("What is the area? (or 'xxx' to exit): ", float, 0, "xxx")
        print("you guessed", guess)
        print()

        if guess == "xxx":
            end_game = "yes"
            break

        # Pretend we've checked users answer
        print("**Check answer**")

    # check if we are out of rounds
    if rounds_played >= rounds:
        break
