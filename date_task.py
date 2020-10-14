from project_task import ProjectTask


class DateTask(ProjectTask):
    def __init__(self, name, task_date):
        super().__init__(name)
        self.task_date = task_date
        self.completed = False

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.completed}, {self.date}'.format(self=self)

    def get_task(self):
        return super().get_task() + " | " + self.task_date
