from date_task import DateTask
from datetime import datetime


class DateListInterface:
    def __init__(self, task_list):
        self.task_list = task_list

    def __repr__(self):
        return f"{self.__class__.__name__}({self.task_list})"

    def add_task(self):
        """Creates a DateTask obj and saves in task_list"""
        while True:
            name = input("Task name: ")
            date_str = input("Task date (dd-mm-yy): ")
            try:
                task = DateTask(name, date_str)
                break
            except ValueError:
                print("Invalid name or date. Try again.")
        self.task_list.append(task)

    def remove_task(self, index):
        """Removes DateTask obj from task_list"""
        del self.task_list[index]

    def view_all_tasks(self, show_numbers=False):
        """Views all tasks in task_list sorted by date, with or without numbers"""
        self.sort_task_list_by_date()
        for i, task in enumerate(self.task_list, start=1):
            if show_numbers:
                print(f"{i}. {task.get_task()}")
            else:
                print(task.get_task())

    def view_task_by_date(self, date_str):
        """Views all tasks by date in string format dd-mm-yy"""
        if self.task_list:
            for task in self.task_list:
                if task.task_date == date_str:
                    print(task.get_task())

    def view_missed_tasks(self):
        """Print all uncompleted tasks from yesterday or older"""
        if self.task_list:
            for task in self.task_list:
                if not task.completed:
                    time = datetime.strptime(task.task_date, "%d-%m-%y")
                    if (datetime.now() - time).days >= 1:
                        print(f"{task.get_task()}")

    def sort_task_list_by_date(self):
        """Sort task_list by date"""
        self.task_list.sort(key=lambda date: datetime.strptime(date.task_date, "%d-%m-%y"))
