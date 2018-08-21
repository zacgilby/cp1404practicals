"""
CP1404 Practical 01
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = float(input("Enter Sales: $"))
    while sales >= 0:
        if sales < 1000:
            sales *= .10
        else:
            sales *= .15
        print("Your bonus is $" + (str(sales)))
        sales = float(input("Enter sales: $"))
    print("That's a negative, pal.")
main()
