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
                print(task.name)
    

class Project:
    def __init__(self, name):
        self.name = name.capitalize()
        self.task_list = []  # store all task objects

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.task_list})'.format(self=self)

    def add_task(self, task):
        pass

    def view_all_tasks(self):
        pass


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
        print("1. Add project")
        print("2. Select project")
        print("3. Quit application")
        value = input("Select: ")

        if value == "1":  # Add project
            li.add_project()
        if value == "2":  # Select project
            li.view_all_lists()
        if value == "3":  # Quit application
            break

if __name__ == '__main__':
    main()
