class ListInterface:
    def __init__(self):
        self.project_lists = []

    def __repr__(self):
        return '{self.__class__.__name__}({self.project_lists})'.format(self=self)

    def add_project(self):
        pass

    def view_all_lists(self):
        pass
    

class Project:
    def __init__(self, name):
        self.name = name.capitalize()
        self.task_list = []  # store all task objects

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.task_list})'.format(self=self)

    def add_task(self, task):
        pass

    def view_all_tasks(self):
        pass


class Task:
    def __init__(self, name):
        self.name = name.capitalize()  # Name of task
        self.completed = False  # If task is done

    def __repr__(self):
        return '{self.__class__.__name__}({self.name}, {self.completed}'.format(self=self)


def main():
    # start of application
    li = ListInterface()


if __name__ == '__main__':
    main()
