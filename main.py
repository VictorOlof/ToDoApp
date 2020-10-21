from project_listinterface import ProjectListInterface
from date_listinterface import DateListInterface
from os import system, name
from datetime import datetime
import pickle

TODAY = datetime.now().strftime("%d-%m-%y")


def clear_window():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def write_sequence_to_file(sequence: list, filename: str):
    """Write a sequence of items from list into a file"""
    with open(filename, "wb") as file:
        for item in sequence:
            pickle.dump(item, file)


def read_sequence_from_file(filename) -> list:
    """Reads a sequence of items from file and returns in a list"""
    sequence = []
    try:
        with open(filename, "rb") as file:
            while True:
                try:
                    item = pickle.load(file)
                    sequence.append(item)
                except EOFError:
                    break
    except FileNotFoundError:
        return sequence
    return sequence


def main():
    # start of application
    p_li = ProjectListInterface(project_list=read_sequence_from_file("project_listinterface.dat"))
    d_li = DateListInterface(task_list=read_sequence_from_file("date_listinterface.dat"))

    while True:
        clear_window()
        print(d_li.task_list)
        print(p_li.project_lists)

        print("Projects:")
        p_li.view_all_lists()
        print()
        print("Tasks for today:")
        d_li.view_task_by_date(TODAY)
        print("Missed tasks:")
        d_li.view_missed_tasks()  # Displays tasks older than today
        print()

        print("1. Add project | 2. Select project")
        print("3. Add task by date | 4. Select task with date")
        value = input("Select option: ")

        if value == "1":  # Add project
            p_li.add_project()

        elif value == "2":  # Select project
            p_li.view_all_lists(show_numbers=True, show_task_list=False)

            selected_project_value = int(input("Select project: "))
            selected_project = p_li.project_lists[selected_project_value - 1]

            while True:
                print(f"You are working with the project:")
                print(selected_project.name)
                selected_project.view_all_tasks(show_numbers=True)
                print()

                print("1. Add task | 2. Mark task | 3. Remove Task | 4. Remove project")
                value = input("Select option (leave blank to stop): ")
                if value == "":
                    break

                elif value == "1":  # Add task
                    selected_project.add_task()

                elif value == "2":  # Mark task
                    selected_task_value = int(input("Select task: "))
                    selected_task = selected_project.task_list[selected_task_value - 1]
                    selected_task.mark_task()  # Set completed to true or false

                elif value == "3":  # Remove task
                    selected_task_value = int(input("Select task: "))
                    selected_project.remove_task(selected_task_value - 1)

                elif value == "4":  # Remove project
                    p_li.remove_project(selected_project_value - 1)
                    break

        elif value == "3":  # Add task by date
            d_li.add_task()

        elif value == "4":  # Select task with date
            while True:
                print("All tasks:")
                d_li.view_all_tasks(show_numbers=True)
                print()

                print("1. Mark task | 2. Remove Task")
                value = input("Select option (leave blank to stop): ")
                if value == "":
                    break

                elif value == "1":  # Mark task
                    selected_task_value = int(input("Select task: "))
                    selected_task = d_li.task_list[selected_task_value - 1]
                    selected_task.mark_task()

                elif value == "2":  # Remove task
                    selected_task_value = int(input("Select task: "))
                    d_li.remove_task(selected_task_value - 1)

        # Save changes to file
        write_sequence_to_file(p_li.project_lists, "project_listinterface.dat")
        write_sequence_to_file(d_li.task_list, "date_listinterface.dat")


if __name__ == '__main__':
    main()
