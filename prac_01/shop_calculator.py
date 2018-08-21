"""
CP1404 Practical 01
Shop calculator that adds up the total cost, if total is above $100 then a 10% discount is
applied before it is displayed.
"""


def main():
    total_price_of_items = 0
    number_of_items = int(input("What are ya buyin', what are ya sellin'?: "))
    while number_of_items <= 0:
        print("Invalid number of items!")
        number_of_items = int(input("What are ya buyin', what are ya sellin'?: "))
    for i in range(0, number_of_items):
        price_of_item = int(input("Price of item " + str(i + 1) + ": $"))
        total_price_of_items += price_of_item
    if total_price_of_items > 100:
        total_price_of_items *= .90
    print("Total price for " + str(number_of_items) + " is $" + str(total_price_of_items))

main()
