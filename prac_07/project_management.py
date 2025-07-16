"""
CP1404/CP5632 Practical
Project management program to load, save, display, filter, add, and update projects.
Estimated time: 50 minutes
Actual time: 80 minutes
"""

import csv
from datetime import datetime
from project import Project


def load_projects(filename):
    """Load projects from a file into a list of Project objects."""
    projects = []
    with open(filename, 'r', newline='') as in_file:
        reader = csv.reader(in_file, delimiter='\t')
        next(reader)  # Skip header
        for row in reader:
            name, start_date, priority, cost_estimate, completion_percentage = row
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                project.priority,
                project.cost_estimate,
                project.completion_percentage
            ])


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_completed()], key=lambda x: x.priority)
    completed = sorted([p for p in projects if p.is_completed()], key=lambda x: x.priority)
    
    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date and display sorted by date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()
    filtered = sorted([p for p in projects if p.starts_after(filter_date)], key=lambda x: x.start_date)
    for project in filtered:
        print(f"  {project}")


def add_project(projects):
    """Add a new project based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion_percentage = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))


def update_project(projects):
    """Update completion percentage and/or priority of a selected project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(f"{projects[choice]}")
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_percentage:
        projects[choice].completion_percentage = int(new_percentage)
    if new_priority:
        projects[choice].priority = int(new_priority)


def main():
    """Main program for project management."""
    default_filename = "project.txt"
    projects = load_projects(default_filename)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {default_filename}")

    while True:
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").lower()
        
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input(f"Would you like to save to {default_filename}? ").lower()
            if save_choice.startswith('y'):
                save_projects(default_filename, projects)
                print(f"Saved {len(projects)} projects to {default_filename}")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
