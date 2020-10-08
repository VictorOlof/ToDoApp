class ListInterface:
    def __init__(self):
        self.project_lists = []

    def __repr__(self):
        return '{self.__class__.__name__}({self.project_lists})'.format(self=self)

    def add_project(self):
        name = input("Enter project name: ")
        project = Project(name)
        self.project_lists.append(project)

    def view_all_lists(self):
        for project in self.project_lists:
            print(project.name)
            for task in project.task_list:
                print(f"  {task.name}")
    

class Project:
    def __init__(self, name):
        self.name = name.capitalize()
        self.task_list = []  # store all task objects

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.task_list})'.format(self=self)

    def add_task(self):
        name = input("Enter task name: ")
        task = Task(name)
        self.task_list.append(task)

    def view_all_tasks(self):
        for task in self.task_list:
            print(f"[{'x' if task.completed else ' '}] {task.name}")


class Task:
    def __init__(self, name):
        self.name = name.capitalize()  # Name of task
        self.completed = False  # If task is done

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.completed}'.format(self=self)


def main():
    # start of application
    li = ListInterface()

    while True:
        li.view_all_lists()

        print("1. Add project")
        print("2. Select project")
        print("3. Quit application")
        value = input("Select: ")

        if value == "1":  # Add project
            li.add_project()
        if value == "2":  # Select project
            li.view_all_lists()

            selected_project_value = int(input("Select the project you want to use: "))
            selected_project = li.project_lists[selected_project_value]
            print(f"You are working with the project: {selected_project.name}")

            print("1. Add task")
            print("2. Delete task")
            value = input("Selected option: ")

            if value == "1":
                selected_project.add_task()
        if value == "3":  # Quit application
            break

if __name__ == '__main__':
    main()
