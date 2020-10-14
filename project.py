from project_task import ProjectTask


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
            task = ProjectTask(name)
            self.task_list.append(task)

    def remove_task(self, index):
        del self.task_list[index]

    def view_all_tasks(self, show_numbers=False):
        for i, task in enumerate(self.task_list, start=1):
            if show_numbers:
                print(f"{i}. {task.get_task()}")
            else:
                print(f"{task.get_task()}")
