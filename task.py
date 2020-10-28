class Task:
    def __init__(self, name):
        self.name = name  # name of task
        self.completed = False  # if task is done

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.completed})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 15:
            raise ValueError("Name of task cannot be longer than 15 chars")
        elif name == "":
            raise ValueError("Name of task cannot be empty.")
        else:
            self._name = name.capitalize().strip()

    def set_completed(self):
        """Sets completed True->False or False->True"""
        if self.completed:
            self.completed = False
        else:
            self.completed = True

    def get_task(self):
        """Return the task information for user in readable string format"""
        return f"[{'x' if self.completed else ' '}] {self.name}"
