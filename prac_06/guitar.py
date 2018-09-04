"""
CP1404/CP5632 Practical
Guitar class with name, year and cost.
"""


class Guitar:
    """Represents Guitar Object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialises a Guiter instance.

        name: string, name of guitar.
        year: integer, ???
        cost: float, price of guitar.
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Returns a string representation of a Guitar object."""
        return "My guitar: {}, first made in {}".format(self.name, self.year)

    def get_age(self):
        age = 2018 - self.year
        return age

    def is_vintage(self, get_age):
        return get_age >= 50
