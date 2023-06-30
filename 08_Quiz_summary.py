# Main Routine...

# NOTE: this component needs the other components to be able to summarize other scenarios and work for unexpected
# cases!!

# TEST CASE SCENARIO...

# Set values for test case
answer = "<correct answer>"
correct_answers = 0
incorrect_answers = 0
rounds_played = 0

# Ask what shape they want 
question_type = input("What shape?")

# Ask how many rounds
rounds_question = input("How many rounds?")

# Set rounds to an integer, so it can be multiplied and divided later on
rounds = int(rounds_question)
print("(continues)")
print()

# Ask question 1, part one, then check answer
question_part = input("Q1 Part One: ")
if question_part == answer:
    correct_answers += 1
    print("Correct!")

else:
    print("Incorrect!")
    incorrect_answers += 1

# Ask question 1, part two, then check answer
question_part = input("Q1 Part Two: ")
if question_part == answer:
    correct_answers += 1
    print("correct!")

else:
    print("Incorrect!")
    incorrect_answers += 1

# One round (question) finished
rounds_played += 1

# Ask question 2, part one, then check answer
question_part = input("Q2 Part One: ")
if question_part == answer:
    correct_answers += 1
    print("correct!")

else:
    print("Incorrect!")
    incorrect_answers += 1

# Ask question 2, part two, then check answer
question_part = input("Q2 Part Two: ")
if question_part == answer:
    correct_answers += 1
    print("correct!")

else:
    print("Incorrect!")
    incorrect_answers += 1

# Two rounds (questions) finished
rounds_played += 1

# Pretend the quiz ends
print()
print("END OF QUIZ")
print()

# GAME SUMMARY...

# Works for all scenarios

# Work out the percentage of questions won
percentage = (correct_answers / (rounds * 2)) * 100

# Convert it into a float so that it can be checked whether it is >= or < 50
success_rate = float(f"{percentage:.2f}")

# Ask user to continue (breaks up the quiz for clarity)
game_summary = input("Enter <any key> to see your Quiz Summary: ")

# When they enter a key, print Quiz Summary statements and stats  
print()
print("*" * 35)
print()
print(" GAME SUMMARY")
print()
print("*" * 35)
print()
print(f"You wanted {rounds} {question_type} questions")
print("-" * 35)
print()
print(f"Total questions attempted: {rounds_played}")
print()
print("-" * 35)
print(f"Correct answers: {correct_answers}")
print(f"Incorrect answers: {incorrect_answers}")
print("-" * 35)
print()
print(f"Success Rate: {success_rate}%")

# If the success rate is greater than or equal to 50, congratulate them!
if success_rate >= 50:
    print("Well done!")

# If it's less than 50%, but grater than 0, give them constructive criticism :)
elif 50 > success_rate > 0:
    print("Theres room for improvement!")

# If its zero, yikes!
elif success_rate == 0:
    print("Yikes!")
