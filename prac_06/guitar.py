"""
CP1404/CP5632 Practical
Guitar class with name, year and cost.
"""

CURRENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:
    """Represents Guitar Object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialises a Guiter instance.

        name: string, name of guitar.
        year: integer, first appearance of the guitar.
        cost: float, price of guitar.
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of a Guitar object."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculates the age of the guitar."""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determines whether a guitar is vintage or not."""
        return self.get_age() >= VINTAGE_AGE
