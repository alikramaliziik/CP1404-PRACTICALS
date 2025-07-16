"""
CP1404/CP5632 Practical
Project class for managing project details.
Estimated time: 30 minutes
Actual time: 37 minutes
"""
from datetime import datetime


class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percentage."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return detailed string representation of a Project."""
        return (f"Project({self.name}, {self.start_date.strftime('%d/%m/%Y')}, "
                f"{self.priority}, {self.cost_estimate}, {self.completion_percentage})")

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_completed(self):
        """Return True if project is 100% complete."""
        return self.completion_percentage == 100

    def starts_after(self, date):
        """Return True if project starts after the given date."""
        return self.start_date > date
