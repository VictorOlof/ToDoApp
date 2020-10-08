class ListInterface:
    def __init__(self):
        self.project_lists = []

    def __repr__(self):
        return '{self.__class__.__name__}({self.project_lists})'.format(self=self)

    def add_project(self):
        name = input("Enter project name: ")
        project = Project(name)
        self.project_lists.append(project)

    def view_all_lists(self, show_numbers=False, show_task_list=True):
        for i, project in enumerate(self.project_lists):
            if show_numbers:
                print(f"{i+1}. {project.name}")
            else:
                print(project.name)

            # show tasks below project name
            if show_task_list:
                if not project.task_list:
                    print(" -empty-")
                else:
                    project.view_all_tasks()
    

class Project:
    def __init__(self, name):
        self.name = name.capitalize()
        self.task_list = []  # store all task objects

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.task_list})'.format(self=self)

    def add_task(self):
        while True:
            name = input("Task name (leave blank to stop): ")
            if name == "":
                break
            task = Task(name)
            self.task_list.append(task)

    def view_all_tasks(self, show_numbers=False):
        for i, task in enumerate(self.task_list):
            if show_numbers:
                print(f"{i+1}. [{'x' if task.completed else ' '}] {task.name}")
            else:
                print(f"[{'x' if task.completed else ' '}] {task.name}")


class Task:
    def __init__(self, name):
        self.name = name.capitalize()  # Name of task
        self.completed = False  # If task is done

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.completed}'.format(self=self)

    def set_completed(self):
        if self.completed:
            self.completed = False
        else:
            self.completed = True


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

                if value == "1":  # Add task
                    selected_project.add_task()
                if value == "2":  # Mark task
                    selected_task_value = int(input("Select task: "))
                    selected_task = selected_project.task_list[selected_task_value-1]
                    selected_task.set_completed()  # Set completed to true or false
        elif value == "3":  # Quit application
            break

if __name__ == '__main__':
    main()
