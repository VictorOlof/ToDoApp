from project.task_project import TaskProject


class TaskProjectList:
    def __init__(self, project_lists):
        self.project_lists = project_lists  # stores all Project objects

    def __repr__(self):
        return f"{self.__class__.__name__}({self.project_lists})'"

    def __len__(self):
        return len(self.project_lists)

    def add_project(self):
        """Creates a Project obj and saves in project_list"""
        while True:
            name = input("Enter project name: ")
            try:
                project = TaskProject(name)
                break
            except ValueError:
                print("Invalid name. Try again.")
        self.project_lists.append(project)

    def remove_project(self, index):
        """Removes Project obj from project_list"""
        del self.project_lists[index]

    def view_all_lists(self, show_numbers=False, show_task_list=True):
        """Views all projects in project_list with or without numbers. With or without tasks below"""
        for i, project in enumerate(self.project_lists, start=1):
            if show_numbers:
                print(f"{i}. {project.name}")
            else:
                print(project.name)

            if show_task_list:
                project.view_all_tasks()
