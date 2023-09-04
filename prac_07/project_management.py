"""
CP1404/CP5632 Practical 7 - Client code to use the Project  class.
Estimate: 2:30 pm
Actual:   45 minutes
"""

import datetime

from prac_07.project import Project

FILENAME = "projects.txt"
DATE_STRING = "20/07/2022"


def main():
    """Project management"""
    projects = []
    menu = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "L":
            read_file(projects)

        elif choice == "S":
            write_file(projects)

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_project(projects)

        elif choice == "A":
            add_new_project(projects)

        elif choice == "U":
            update_percentage(projects)

        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def read_file(projects):
    """read the file.txt"""
    try:
        with open(FILENAME, "r") as in_file:
            lines = in_file.readlines()
            for line in lines[1:]:
                parts = line.strip().split("\t")
                date_string = parts[1]
                date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
                project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
    except FileNotFoundError:
        print("File not found.")


def write_file(projects):
    """write the file.txt"""
    try:
        with open(FILENAME, "w") as out_file:
            out_file.write("Name\tDate\tPriority\tCost\tPercentage\n")
            for project in projects:
                out_file.write(str(project) + "\n")
    except FileNotFoundError:
        print("File not found.")


def display_projects(projects):
    """Display Uncompleted project and Completed project"""
    space = "  "

    print("Incomplete projects:")
    for project in projects:
        if not project.is_completed():
            print(f"{space}{project}")

    print("Completed projects:")
    for project in projects:
        if project.is_completed():
            print(f"{space}{project}")


def filter_project(projects):
    """filter the project date after the date_string from newest to oldest"""
    date_string = "20/07/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.date > date]

    filtered_projects.sort()

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """ask for the input for the new project"""

    print("Let's add a new project")
    name = input("Name: ")

    start_date = get_valid_date("Start date (dd/mm/yyyy): ")

    priority = int(input("Priority: "))
    cost = int(input("Cost estimate: $"))
    percent = int(input("Percent complete: "))

    projects.append(Project(name, start_date, priority, cost, percent))


def update_percentage(projects):
    """update the completed percentage of project"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    while True:
        try:
            project_choice = int(input("Project choice: "))
            print(projects[project_choice])

            new_percentage = int(input("New Percentage: "))
            projects[project_choice].update_percentage(new_percentage)

            print("New Priority: ")

        except ValueError:
            print("Invalid input (only index is acceptable)")


def get_valid_date(date):
    """Get the valid date"""
    is_finished = False

    while not is_finished:
        date_string = input(date)

        try:
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_finished = True
            return date

        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")


main()
