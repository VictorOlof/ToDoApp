from task import Task
from datetime import datetime


class DateTask(Task):
    def __init__(self, name, task_date):
        super().__init__(name)
        self.task_date = task_date
        self.completed = False

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.completed}, {self.task_date}'.format(self=self)

    @property
    def task_date(self):
        return self._task_date.strftime("%d-%m-%y")

    @task_date.setter
    def task_date(self, date_str):
        self._task_date = datetime.strptime(date_str, "%d-%m-%y")

    def get_task(self):
        return f"[{'x' if self.completed else ' '}] {self.name} | {self.task_date}"
