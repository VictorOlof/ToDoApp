from project import Project
from read_write_file import read


class ListInterface:
    def __init__(self):
        self.project_lists = read()  # stores all Project objects

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
        for i, project in enumerate(self.project_lists):
            if show_numbers:
                print(f"{i+1}. {project.name}")
            else:
                print(project.name)

            # print tasks below project name
            if show_task_list:
                if not project.task_list:
                    print(" -empty-")
                else:
                    project.view_all_tasks()
