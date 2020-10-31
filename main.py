from projectlist.task_project_list import TaskProjectList
from date_project import DateProject
from habit_project import HabitProject
from os import system, name
from datetime import datetime
import pickle

TODAY = datetime.now().strftime("%d-%m-%y")


def clear_window():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
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
    """Prints all items in a tuple with number"""
    for i, option in enumerate(options):
        print(f"{i + 1}. {options[i]}")


def menu_get_option(options: tuple):
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
    task_proj_list = TaskProjectList(project_lists=read_sequence_from_file("project_listinterface.dat"))
    date_proj = DateProject(task_list=read_sequence_from_file("date_project.dat"))
    habit_proj = HabitProject(task_list=read_sequence_from_file("habit_project.dat"))

    while True:
        clear_window()
        print(date_proj.task_list)
        print(task_proj_list.project_lists)

        print("Projects:")
        task_proj_list.view_all_lists()
        print()
        print("Tasks for today:")
        date_proj.view_task_by_date(TODAY)
        print()
        print("Missed tasks:")
        date_proj.view_missed_tasks()  # Displays tasks older than today
        print()
        print("Habits for today:")
        habit_proj.view_task_by_date(TODAY)
        print()

        menu_options = (
            "Add project",
            "Project options",
            "Add task by date",
            "Date task options",
            "Add habit",
            "Habit options"
        )
        menu_view(menu_options)
        option = menu_get_option(menu_options)

        if option == 1:  # Add project
            task_proj_list.add_project()

        elif option == 2:  # Select project
            task_proj_list.view_all_lists(show_numbers=True, show_task_list=False)

            selected_project_value = int(input("Select project: "))
            selected_project = task_proj_list.project_lists[selected_project_value - 1]

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
                    task_proj_list.remove_project(selected_project_value - 1)
                    break

                elif option == 5:  # Leave menu
                    break

        elif option == 3:  # Add task by date
            date_proj.add_task()

        elif option == 4:  # Select task with date
            while True:
                clear_window()
                print("All tasks:")
                date_proj.view_all_tasks(show_numbers=True)
                print()

                menu_options = (
                    "Mark task",
                    "Remove Task",
                    "Leave menu"
                )
                menu_view(menu_options)
                option = menu_get_option(menu_options)

                if option == 1:  # Mark task
                    date_proj.mark_task()

                elif option == 2:  # Remove task
                    date_proj.remove_task()

                elif option == 3:  # Leave menu
                    break

        elif option == 5:  # Add habit
            habit_proj.add_task()

        elif option == 6:  # Select habit
            while True:
                clear_window()
                print("All habits:")
                habit_proj.view_all_tasks(show_numbers=True)
                print()

                menu_options = (
                    "Mark task",
                    "Remove Task",
                    "Leave menu"
                )
                menu_view(menu_options)
                option = menu_get_option(menu_options)

                if option == 1:  # Mark task
                    habit_proj.mark_task()

                elif option == 2:  # Remove task
                    habit_proj.remove_task()

                elif option == 3:  # Leave menu
                    break

        # Save changes to file
        write_sequence_to_file(task_proj_list.project_lists, "project_listinterface.dat")
        write_sequence_to_file(date_proj.task_list, "date_project.dat")
        write_sequence_to_file(habit_proj.task_list, "habit_project.dat")


if __name__ == '__main__':
    main()
