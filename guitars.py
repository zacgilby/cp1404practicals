"""
CP1404/CP5632 Practical
Guitar stuff
"""

from prac_06.guitar import Guitar

guitars = []

print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    add_guitar = Guitar(name, year, cost)
    guitars.append(add_guitar)
    print("{} added.".format(add_guitar))
    name = input("Name: ")

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

# TODO: TypeError when exiting while loop, find solution since the solution doesn't work.

guitars.sort()
print("These are my guitars:")

if guitars is not None:
    for i, guitar in enumerate(guitars):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print("Guitar {0}: {1.name:>30} ({1.year}), worth ${1.cost:10,.2f}\
             {2}".format(i + 1, guitar, vintage_string))
else:
    print("No guitars :( Quick, go and buy one!")
