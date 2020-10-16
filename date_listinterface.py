import pickle
from date_task import DateTask


class DateListInterface:
    def __init__(self):
        self.task_list = self.read_from_file()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.task_list})"

    def add_task(self):
        """Creates a DateTask obj and saves in task_list"""
        name = input("Task name: ")
        date_str = input("Task date (dd-mm-åå): ")

        task = DateTask(name, date_str)
        self.task_list.append(task)

    def remove_task(self, index):
        """Removes DateTask obj from task_list"""
        del self.task_list[index]

    def view_all_tasks(self, show_numbers=False):
        """Views all tasks in task_list with or without numbers"""
        for i, task in enumerate(self.task_list, start=1):
            if show_numbers:
                print(f"{i}. {task.get_task()}")
            else:
                print(f"{task.get_task()}")

    def view_task_by_date(self, date_str):
        """Views all tasks by date in string format dd-mm-yy"""
        if self.task_list:
            for i, task in enumerate(self.task_list, start=1):
                if task.task_date == date_str:
                    print(f"{task.get_task()}")
        else:
            print(" -empty-")

    @staticmethod
    def read_from_file():
        """Return all DateTask objects from file"""
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
        """Write all DateTask object to file"""
        with open("date_tasks.dat", "wb") as date_tasks_file:
            for task in task_list:
                pickle.dump(task, date_tasks_file)
