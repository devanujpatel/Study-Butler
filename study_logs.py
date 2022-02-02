import verify_input


def my_init():
    print("Welcome to Study Logs Menu.")

    while True:
        print("--------Study Logs Menu--------")
        print("Enter [1] to enter new logs")
        print("Enter [2] to edit logs")
        print("Enter [3] to view logs")
        print("Enter [4] to go to Home Menu")
        # allow option to filter logs by date

        user_input = input("Enter numeric choice: ")
        clean_input, user_input = verify_input.very_input(user_input, [1, 2, 3, 4])

        if not clean_input:
            print("Invalid input")
            continue

        if user_input == 1:
            # enter new logs
            pass
        elif user_input == 2:
            # edit logs
            pass
        elif user_input == 3:
            # view logs
            pass
        elif user_input == 4:
            # go to home menu
            break

    return None
