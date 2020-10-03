from datetime import date


TODAY = date.today().strftime('%d-%m-%y')


class TodoList:
    def __init__(self):
        self.todo_list = []  # store all task objects

    def __repr__(self):
        return '{self.__class__.__name__}({self.todo_list})'.format(self=self)

    def add_task(self, task):
        # put task object in todo_list
        self.todo_list.append(task)

    def show_todo_list(self, date_input):
        # returns the todolist with task objects stored in todos
        for item in self.todo_list:
            if item.expire_date == date_input:
                print(item.completed, "-", item.task_name)
        # TODO: loop with enumerate for user to navigate?


class Task:
    def __init__(self, task_name, expire_date):
        self.task_name = task_name.capitalize()  # name of task
        self.expire_date = expire_date  # date for task to show up
        self.completed = False  # if task is done

    def __repr__(self):
        return '{self.__class__.__name__}({self.task_name}, {self.expire_date}, {self.completed})'.format(self=self)


def main():
    # start of application
    todolist = TodoList()  # create a todolist using TodoList class

    running = True
    while running:
        # show todolist
        todolist.show_todo_list(TODAY)

        # show menu
        choice = int(input("1-Quit 2-Input task "))

        if choice == 1:  # quit application
            running = False

        elif choice == 2:  # input a new task
            task = Task(input("Input task: "), TODAY)
            todolist.add_task(task)


if __name__ == '__main__':
    main()
