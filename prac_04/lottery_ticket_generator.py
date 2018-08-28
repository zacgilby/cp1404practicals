"""
CP1404/CP5632 - Practical
Randomly generates a quick pick game chosen by the user..
"""

from random import randint

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Come on, at least one game!")
        number_of_quick_picks = int(input("How many quick picks? "))
    generate_quick_pick(number_of_quick_picks)


def generate_quick_pick(number_of_quick_picks):
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
