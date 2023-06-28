actual_ans = 2.5542454
rounded_ans = f"{actual_ans:.2f}"

user_ans = 2.55
rounded_user_ans = f"{user_ans:.2f}"

if actual_ans == user_ans:
    print("raw match")
elif rounded_ans == rounded_user_ans:
    print("rounded match")
    print(actual_ans * 2)
    print(rounded_ans * 2)
    print(user_ans * 2)
    print(rounded_user_ans * 2)
else:
    print("epic fail")
