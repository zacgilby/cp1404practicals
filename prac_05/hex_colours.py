"""
CP1404/CP5632 - Practical
This program will allow users to search for hexadecimal colour codes by using the colours name.
"""

HEX_COLOUR_NAMES_TO_HEX_COLOUR_CODES = {"black": "#000000", "brown": "#a52a2a", "coral": "#ff7f50",
                                        "firebrick": "#b22222", "gray": "#bebebe", "lavender": "#e6e6fa",
                                        "magenta": "#ff00ff", "maroon": "#b03060", "medium": "#66cdaa",
                                        "moccasin": "#ffe4b5", "orchid": "#da70d6", "pink": "#ffc0cb",
                                        "rebeccapurple": "#663399", "salmon": "#fa8072"}
# for name, code in HEX_COLOUR_NAMES_TO_HEX_COLOUR_CODES.items():
#     print("The hexadecimal code for {:13} is {}".format(name, code))

name = input("Enter a colour: ").lower()
while name != "":
    if name in HEX_COLOUR_NAMES_TO_HEX_COLOUR_CODES:
        print("The hex code for {} is {}".format(name, HEX_COLOUR_NAMES_TO_HEX_COLOUR_CODES[name]))
    else:
        print("That's an invalid colour!")
    name = input("Enter a colour: ").lower()


