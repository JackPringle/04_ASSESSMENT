# Functions...

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


# Main routine...

# Ask the questions question, set mode to nothing
rounds_played = 0
rounds = num_check("How many questions?: ", int, 0, exit_code="")
mode = None

# If user enters <enter> start infinite mode
if rounds == "":
    mode = "infinite"
    rounds = 5

# Rounds loop
end_quiz = "no"
while end_quiz == "no":

    # Calculate rounds played for infinite mode
    if mode == "infinite":
        heading = f"Question {rounds_played + 1} (infinite mode)"
        rounds += 1

    # If mode is not infinite, calculate rounds played against total rounds
    else:
        heading = f"Question {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    # Show question and ask user for answer
    print("**Question goes here**")
    print()
    guess = num_check("What is the area? (or 'xxx' to exit): ", float, 0, "xxx")
    print("you guessed", guess)
    print()

    # Check for exit code
    if guess == "xxx":
        end_quiz = "yes"

    # If exit code is entered, end
    if end_quiz == "yes":
        print("You have ended the quiz")
        break

    # Pretend we've checked users answer
    print("**Check answer**")
    print()

    # Check if we are out of rounds
    # If out of rounds, end rounds loop
    if rounds_played >= rounds:
        print("Out of rounds!")
        break
