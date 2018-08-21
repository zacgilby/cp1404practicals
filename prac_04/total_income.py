"""
A program that calculates the cumulative amount of income over a number of months and displays it in a report format..
"""


def main():
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(number_of_months):
        monthly_income = float(input("Enter income for month {}: ".format(month + 1)))
        incomes.append(monthly_income)
    display_income_report(number_of_months, incomes)


def display_income_report(number_of_months, incomes):
    print("\nIncome Report\n-------------")
    total_income = 0
    for month in range(number_of_months):
        monthly_income = incomes[month]
        total_income += monthly_income
        print("Month {} - This months income: ${} Total income: ${}".format(month + 1, monthly_income, total_income))


main()
