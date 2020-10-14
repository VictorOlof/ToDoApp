from project import Project
import pickle


class ProjectListInterface:
    def __init__(self):
        self.project_lists = self.read_from_file()  # stores all Project objects

    def __repr__(self):
        return '{self.__class__.__name__}({self.project_lists})'.format(self=self)

    def add_project(self):
        name = input("Enter project name: ")
        project = Project(name)
        self.project_lists.append(project)

    def remove_project(self, index):
        del self.project_lists[index]

    def view_all_lists(self, show_numbers=False, show_task_list=True):
        # print projects name
        for i, project in enumerate(self.project_lists, start=1):
            if show_numbers:
                print(f"{i}. {project.name}")
            else:
                print(project.name)

            # print tasks below project name
            if show_task_list:
                if not project.task_list:
                    print(" -empty-")
                else:
                    project.view_all_tasks()

    @staticmethod
    def read_from_file():
        tasks = []
        try:
            with open("date_tasks.dat", "rb") as date_tasks_file:
                while True:
                    try:
                        task = pickle.load(date_tasks_file)
                        tasks.append(task)
                    except EOFError:
                        break
        except FileNotFoundError:
            return tasks
        return tasks

    @staticmethod
    def write_to_file(task_list: list):
        with open("date_tasks.dat", "wb") as date_tasks_file:
            for task in task_list:
                pickle.dump(task, date_tasks_file)
