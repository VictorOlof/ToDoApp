from task import Task


class Project:
    def __init__(self, name):
        self.name = name  # name of project
        self.task_list = []  # store all task objects

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.task_list})"

    def __len__(self):
        return len(self.task_list)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 15:
            raise ValueError("Name of project cannot be longer than 15 chars")
        elif name == "":
            raise ValueError("Name of project cannot be empty.")
        else:
            self._name = name.capitalize().strip()

    def add_task(self):
        """Creates a Task obj and saves in task_list"""
        while True:
            name = input("Task name: ")
            try:
                task = Task(name)
                break
            except ValueError:
                print("Invalid name. Try again.")
        self.task_list.append(task)

    def remove_task(self, index):
        """Removes Task obj from task_list"""
        del self.task_list[index]

    def view_all_tasks(self, show_numbers=False):
        """Views all tasks in task_list with or without numbers"""
        if self.task_list:
            for i, task in enumerate(self.task_list, start=1):
                if show_numbers:
                    print(f"{i}. {task.get_task()}")
                else:
                    print(f"{task.get_task()}")
        else:
            print(" -empty-")
