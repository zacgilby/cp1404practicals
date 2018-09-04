"""
CP1404/CP5632 Practical
Programming language class.
"""


class ProgrammingLanguage:
    """Represents a programming language."""

    def __init__(self, field, typing, reflection, year):
        """"Initialises a ProgrammingLanguage instance.

        field: string, name of programming language.
        typing: boolean, static or dynamic typing.
        reflection: string/boolean? yes or no.
        year: string, birth year of the programming language.
        """

        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """"Return string representation of a ProgrammingLanguage."""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """"Returns a boolean based on the typing of the programming language."""
        return self.typing == "Dynamic"
