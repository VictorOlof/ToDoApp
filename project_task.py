class ProjectTask:
    def __init__(self, name):
        self.name = name.capitalize()  # name of task
        self.completed = False  # if task is done

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.completed}'.format(self=self)

    def set_completed(self):
        # set completed from True -> False or False -> True
        if self.completed:
            self.completed = False
        else:
            self.completed = True

    def get_task(self):
        return f"[{'x' if self.completed else ' '}] {self.name}"
