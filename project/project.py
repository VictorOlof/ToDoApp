from task.task import Task
from project.project_interface import ProjectInterface


class Project(ProjectInterface):
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
        if not isinstance(name, str):
            raise TypeError("Name of project needs be type of str")
        if len(name) > 25:
            raise ValueError("Name of project cannot be longer than 25 characters")
        elif name == "":
            raise ValueError("Name of project cannot be empty.")
        else:
            self._name = name.capitalize().strip()

    def add_task(self):
        while True:
            name = input("Task name: ")
            try:
                task = Task(name)
                break
            except ValueError:
                print("Invalid name. Try again.")
        self.task_list.append(task)

    def remove_task(self):
        while True:
            selected_task_value = input("Select task: ")
            try:
                if selected_task_value == "0":
                    raise IndexError
                del self.task_list[int(selected_task_value) - 1]
                break
            except (ValueError, IndexError):
                print("Invalid choice.")

    def mark_task(self):
        while True:
            selected_task_value = input("Select task: ")
            try:
                if selected_task_value == "0":
                    raise IndexError
                selected_task = self.task_list[int(selected_task_value) - 1]
                selected_task.set_completed()
                break
            except (ValueError, IndexError):
                print("Invalid choice.")

    def view_all_tasks(self, show_numbers=False):
        if self.task_list:
            for i, task in enumerate(self.task_list, start=1):
                if show_numbers:
                    print(f"{i}. {task.get_task()}")
                else:
                    print(f"{task.get_task()}")
        else:
            print(" -empty-")

