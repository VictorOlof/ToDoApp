"""
This module read and write project objects from/to projects.dat file during startup and exit of application.
"""

import pickle


def save(projects_list: list):
    # save list of projects_objects to file
    with open("projects.dat", "wb") as project_file:
        for project in projects_list:
            pickle.dump(project, project_file)


def read():
    # load projects file from file and store in list
    projects = []
    try:
        with open("projects.dat", "rb") as project_file:
            while True:
                try:
                    project = pickle.load(project_file)
                    projects.append(project)
                except EOFError:
                    break
    except FileNotFoundError:
        return projects
    return projects
