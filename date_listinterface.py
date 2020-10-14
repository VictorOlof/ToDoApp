import pickle
from date_task import DateTask


class DateListInterface:
    def __init__(self):
        self.task_list = self.read_from_file()

    def __repr__(self):
        return '{self.__class__.__name__}({self.task_list})'.format(self=self)

    def add_task(self):
        name = input("Task name: ")
        task_date = input("Task date (dd-mm-åå): ")
        task = DateTask(name, task_date)
        self.task_list.append(task)

    def remove_task(self, index):
        del self.task_list[index]

    def view_all_tasks(self, show_numbers=False):
        for i, task in enumerate(self.task_list, start=1):
            if show_numbers:
                print(f"{i}. {task.get_task()}")
            else:
                print(f"{task.get_task()}")

    def view_task_by_date(self, date):
        for i, task in enumerate(self.task_list, start=1):
            if task.task_date == date:
                print(f"{task.get_task()}")

    @staticmethod
    def read_from_file():
        tasks = []
        try:
            with open("date_tasks.dat", "rb") as date_tasks_file:
                while True:
                    try:
                        task = pickle.load(date_tasks_file)
                        tasks.append(task)
                    except EOFError:
                        break
        except FileNotFoundError:
            return tasks
        return tasks

    @staticmethod
    def write_to_file(task_list: list):
        with open("date_tasks.dat", "wb") as date_tasks_file:
            for task in task_list:
                pickle.dump(task, date_tasks_file)
