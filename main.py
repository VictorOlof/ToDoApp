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


def menu_view(options: tuple):
    for i, option in enumerate(options):
        print(f"{i + 1}. {options[i]}")


def menu_get_option(options):
    while True:
        try:
            option = int(input("Select option: "))
            if 1 <= option <= len(options):
                return option
            else:
                raise ValueError
        except ValueError:
            print("Invalid option.")


def main():
    # start of application
    p_li = ProjectListInterface(project_lists=read_sequence_from_file("project_listinterface.dat"))
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

        menu_options = (
            "Add project",
            "Select project",
            "Add task by date",
            "Select task with date"
        )
        menu_view(menu_options)
        option = menu_get_option(menu_options)

        if option == 1:  # Add project
            p_li.add_project()

        elif option == 2:  # Select project
            p_li.view_all_lists(show_numbers=True, show_task_list=False)

            selected_project_value = int(input("Select project: "))
            selected_project = p_li.project_lists[selected_project_value - 1]

            while True:
                clear_window()
                print(f"You are working with the project:")
                print(selected_project.name)
                selected_project.view_all_tasks(show_numbers=True)
                print()

                menu_options = (
                    "Add task",
                    "Mark task",
                    "Remove Task",
                    "Remove project",
                    "Leave menu"
                )
                menu_view(menu_options)
                option = menu_get_option(menu_options)

                if option == 1:  # Add task
                    selected_project.add_task()

                elif option == 2:  # Mark task
                    selected_project.mark_task()

                elif option == 3:  # Remove task
                    selected_project.remove_task()

                elif option == 4:  # Remove project
                    p_li.remove_project(selected_project_value - 1)
                    break

                elif option == 5:  # Leave menu
                    break

        elif option == 3:  # Add task by date
            d_li.add_task()

        elif option == 4:  # Select task with date
            while True:
                clear_window()
                print("All tasks:")
                d_li.view_all_tasks(show_numbers=True)
                print()

                menu_options = (
                    "Mark task",
                    "Remove Task",
                    "Leave menu"
                )
                menu_view(menu_options)
                option = menu_get_option(menu_options)

                if option == 1:  # Mark task
                    d_li.mark_task()

                elif option == 2:  # Remove task
                    d_li.remove_task()

                elif option == 3:  # Leave menu
                    break

        # Save changes to file
        write_sequence_to_file(p_li.project_lists, "project_listinterface.dat")
        write_sequence_to_file(d_li.task_list, "date_listinterface.dat")


if __name__ == '__main__':
    main()
