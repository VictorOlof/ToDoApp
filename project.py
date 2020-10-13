from task import Task


class Project:
    def __init__(self, name):
        self.name = name.capitalize()  # name of project
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
                print(f"{i+1}. {task.get_task()}")
            else:
                print(f"{task.get_task()}")
