from listinterface import ListInterface


def main():
    # start of application
    li = ListInterface()

    while True:
        li.view_all_lists()
        print()

        print("1. Add project | 2. Select project | 3. Quit")
        value = input("Select option: ")
        if value == "1":  # Add project
            li.add_project()
        elif value == "2":  # Select project
            li.view_all_lists(show_numbers=True, show_task_list=False)

            selected_project_value = int(input("Select project: "))
            selected_project = li.project_lists[selected_project_value-1]
            while True:
                print(f"You are working with the project:")
                print(selected_project.name)
                selected_project.view_all_tasks(show_numbers=True)
                print()

                print("1. Add task | 2. Mark task")
                value = input("Select option (leave blank to stop): ")
                if value == "":
                    break
                elif value == "1":  # Add task
                    selected_project.add_task()
                elif value == "2":  # Mark task
                    selected_task_value = int(input("Select task: "))
                    selected_task = selected_project.task_list[selected_task_value-1]
                    selected_task.set_completed()  # Set completed to true or false
        elif value == "3":  # Quit application
            break

if __name__ == '__main__':
    main()
