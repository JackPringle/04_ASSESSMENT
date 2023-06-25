# String checker function
def string_checker(question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(question).lower()

        # Check the string is in the valid list
        for item in valid_list:

            # Check if the response matches the entire item or just the first character
            # of the item (if it's not empty)
            if response == item or (len(item) > 0 and response == item[0]):
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
