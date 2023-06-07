# String checker function
def string_checker(question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(question).lower()

        # Check the string is in the valid list
        for item in valid_list:
            if response == item or response == item[0]:
                print("program continues")
                return item

        # If not in valid list, print error
        print(error)
        print()


# Main routine...

# List of valid response
yes_no_list = ["yes", "no"]
rtc_list = ["rectangle", "triangle", "circle", "xxx"]

# QUESTION
played_before = string_checker("R / T / C? ",
                               rtc_list, "Please enter r / t / c")
