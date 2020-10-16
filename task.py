class Task:
    def __init__(self, name):
        self.name = name.capitalize()  # name of task
        self.completed = False  # if task is done

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.completed}"

    def set_completed(self):
        """Sets completed True->False or False->True"""
        if self.completed:
            self.completed = False
        else:
            self.completed = True

    def get_task(self):
        """Return the task information for user in readable format"""
        return f"[{'x' if self.completed else ' '}] {self.name}"
