"""
CP1404 Practical 01
Fixed program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    print(result_calculator(score))


def result_calculator(score):
    if score < 0 or score > 100:
        score = "Invalid score."
    elif score >= 90:
        score = "Excellent"
    elif score >= 50:
        score = "Passable"
    else:
        score = "Bad"
    return score


main()
