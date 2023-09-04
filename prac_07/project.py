COMPLETED_PERCENTAGE = 100


class Project:
    """Represent information about a programming language."""

    def __init__(self, name="", date=None, priority=0, cost=0.0, percentage=0):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __lt__(self, other):
        """sort the date from the oldest to newest"""
        return self.date < other.date

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        formatted_date = self.date.strftime("%d/%m/%Y") if self.date else "N/A"
        return f"{self.name}, {formatted_date}, priority {self.priority}, estimate: ${self.cost}, completion: {self.percentage}%"

    def is_completed(self):
        """define the self.percentage as 100"""
        return self.percentage == COMPLETED_PERCENTAGE

    def update_percentage(self, new_percentage):
        """define the input of percentage to be new percentage"""
        return self.percentage == new_percentage
