from task.task_project import ProjectTask
from datetime import datetime


class DateTask(ProjectTask):
    def __init__(self, name, task_date):
        super().__init__(name)
        self.task_date = task_date

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.completed}, {self.task_date}'""

    @property
    def task_date(self):
        """Return the date in string format dd-mm-yy"""
        return self._task_date.strftime("%d-%m-%y")

    @task_date.setter
    def task_date(self, date_str):
        """Takes date in format dd-mm-yy and saves it as a datetime object"""
        self._task_date = datetime.strptime(date_str, "%d-%m-%y")

    def get_task(self):
        """Return the task information for user in readable format"""
        return f"{super().get_task()} | {self.task_date}"
