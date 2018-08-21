"""
CP1404 Practical 01
Loops, counting in 1s, 10s and down from 20 to 1.
"""

def main():
    # for i in range(1, 21, 2):
    #     print(i, end=' ')
    # print()

    # for i in range(0, 101, 10):
    #     print(i, end=' ')
    # print()

    # for i in range(20, 0, -1):
    #     print(i, end=' ')
    # print()

    number_of_stars = int(input("Number of stars: "))
    for i in range(number_of_stars):
        print("*", end=' ')
    print()

    for i in range(number_of_stars):
        print("*" * (i + 1), end=' ')
    print()
main()
