# Integer checker function

def int_check(question, type, low=None, exit_code=None):
    if low is None:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()

        try:
            response = type(response)
            if response == exit_code:
                return response

            elif response < low :
                error = "Please enter a number more than 0"

            elif response < low:
                error = "Please enter a number more than 0"

            else:
                return response

            except ValueError:
                print(error)


quiz = int_check("Please enter the area: ", int, None, "xxx")
