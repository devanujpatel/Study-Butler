import json

from tabulate import tabulate

import verify_input


def show_table(study_logs):
    table = tabulate(study_logs["study_logs"], headers=['Index', 'Name', 'Date', 'Hours'], tablefmt='pretty')
    print(table)


def take_log_info():
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

    return log_name, log_date, hours


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
            log_name, log_date, hours = take_log_info()

            with open("study_logs.json", "r") as db:
                study_logs = json.loads(db.read())
                if study_logs["study_logs"]:
                    last_index = int(study_logs["study_logs"][-1][0])
                else:
                    last_index = 0

                study_logs["study_logs"].append([last_index+1, log_name, log_date, hours])

            with open("study_logs.json", "w") as db:
                db.write(json.dumps(study_logs, indent=4))
            print("Log successfully entered.")

        elif user_input == 2:
            # edit logs
            with open("study_logs.json", "r") as db:
                study_logs = json.loads(db.read())

            show_table(study_logs)
            try:
                num = int(input("Enter index of log to be edited: "))
            except ValueError:
                print("Invalid input!")
                continue

            print(num)
            log_name, log_date, hours = take_log_info()
            count = 0
            for log in study_logs["study_logs"]:
                print(log[0], num)
                if int(log[0]) == num:
                    study_logs['study_logs'][count][1] = log_name
                    study_logs['study_logs'][count][2] = log_date
                    study_logs['study_logs'][count][3] = hours
                    break
            print(study_logs)
            with open("study_logs.json", "w") as db:
                db.write(json.dumps(study_logs, indent=4))
            print("Log successfully entered.")

        elif user_input == 3:
            # view logs
            with open("study_logs.json", "r") as db:
                study_logs = json.loads(db.read())

            show_table(study_logs)

        elif user_input == 4:
            # go to home menu
            break

    return None
