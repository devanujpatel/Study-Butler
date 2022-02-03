import json

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
            log_name = input("Enter log name: ")
            log_date = input("Enter date in dd/mm/yyyy format: ")

            while True:

                hours = input("Number of hours studied: ")
                try:
                    hours = float(hours)
                    break
                except ValueError:
                    print("Invalid input")
                    continue

            with open("database.json", "r") as db:
                study_logs = json.loads(db.read())
                print(study_logs)
                study_logs["study_logs"].append({"name": log_name, "date": log_date, "hours": hours})

            with open("database.json", "w") as db:
                db.write(json.dumps(study_logs, indent=4))

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
