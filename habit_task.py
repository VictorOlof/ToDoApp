from task import Task
from datetime import datetime, timedelta


class HabitTask(Task):
    def __init__(self, name, repeat):
        super().__init__(name)
        self.repeat = repeat
        self.days_completed = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.completed}, {self.task_date})'""

    @property
    def repeat(self):
        return self._repeat

    @repeat.setter
    def repeat(self, number):
        if not number.isdigit():
            raise ValueError("Repeat needs to be a digit")
        elif 1 > int(number) > 7:
            raise ValueError("Repeat need to be in range 1..7")
        else:
            self._repeat = int(number)

    @property
    def task_date(self):
        """ger datum till kommande weekday"""
        return self.calc_next_habit_date(self._repeat).strftime("%d-%m-%y")

    @staticmethod
    def calc_next_habit_date(repeat_day):
        """Calculates days left to the repeat day, returns calculated repeat date"""
        today = datetime.today()
        habit_date = datetime.today()

        if today.isoweekday() == repeat_day:
            return habit_date
        elif repeat_day > today.isoweekday():
            days_left = abs(repeat_day - today.isoweekday())
            habit_date = today + timedelta(days=days_left)
        else:
            days_left = (7 - today.isoweekday()) + repeat_day
            habit_date = today + timedelta(days=days_left)
        return habit_date

    def set_completed(self):
        """Sets completed True->False or False->True
        and adds or remove completed date to days_completed"""
        if datetime.today().strftime("%d-%m-%y") in self.days_completed:
            self.remove_day_completed(datetime.today())
        else:
            self.add_day_completed(datetime.today())

    def get_completed(self):
        """Only return True if repeat day is today and task is done"""
        today = datetime.today()
        if today.isoweekday() == self._repeat:
            if today.strftime("%d-%m-%y") in self.days_completed:
                return True
        return False

    def add_day_completed(self, day):
        self.days_completed.append(day.strftime("%d-%m-%y"))

    def remove_day_completed(self, date):
        self.days_completed.remove(date.strftime("%d-%m-%y"))

    def get_task(self):
        """Return the task information for user in readable format"""
        return f"[{'x' if self.get_completed() else ' '}] {self.name} | [{self._repeat}] | {self.days_completed}"
