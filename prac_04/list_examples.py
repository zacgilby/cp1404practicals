# 5 number list
numbers = []

print("Please enter 5 numbers below.")
for i in range(0, 5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
print("The average of the numbers is {}".format(sum(numbers) / len(numbers)))

# Woefully inadequate security checker...
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
yourname = input("Enter your name: ")
if yourname in usernames:
    print("Access granted.")
else:
    print("Access denied.")
