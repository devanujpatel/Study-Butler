import study_logs  # , planner.py, exams.py
import verify_input

ask_input = True
print("Welcome to Study Butler")
while ask_input:
    print("--------Home Menu--------")
    print("Enter [1] for Study Logs menu.")
    print("Enter [2] to open Planner.")
    print("Enter [3] for Exams section.")
    print("Enter [4] to exit.")

    user_input = input("Enter numeric choice: ")
    clean_input, user_input = verify_input.very_input(user_input, [1, 2, 3, 4])

    if not clean_input:
        print("Invalid input")
        continue

    if user_input == 1:
        study_logs.my_init()

    elif user_input == 4:
        print("Goodbye!")
        break
