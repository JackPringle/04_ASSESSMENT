# Number checker function...

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


# Main Routine...

# Question types
quiz = num_check("Please enter an integer: ", int, exit_code="xxx")
thing = num_check("Please enter a float: ", float, 0, "xxx")
