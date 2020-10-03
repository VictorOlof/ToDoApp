class TodoList:
    def __init__(self):
        self.todo_list = []  # store all task objects

    def add_task(self, task):
        # put task object in todo_list
        self.todo_list.append(task)

    def show_todo_list(self):
        # returns the todolist with task objects stored in todos
        for item in self.todo_list:
            print(item.completed, "-", item.task_name)


class Task:
    def __init__(self, task_name):
        self.task_name = task_name.capitalize()  # Name of task
        self.completed = False  # If task is done


def main():
    # start of application
    todolist = TodoList()  # create a todolist using TodoList class

    running = True
    while running:
        # show todolist
        todolist.show_todo_list()

        # show menu
        choice = int(input("1-Quit 2-Input task "))

        if choice == 1:  # quit application
            running = False

        elif choice == 2:  # input a new task
            task = Task(input("Input task: "))
            todolist.add_task(task)


if __name__ == '__main__':
    main()
