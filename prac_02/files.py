"""
Ask the user for their name and write it to a file called "name.txt"
"""

OUTPUT_FILE = "name.txt"
out_file = open(OUTPUT_FILE, 'w')
print("Bob", file=out_file)
out_file.close()

in_file = open(OUTPUT_FILE, 'r')
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

in_file = open("numbers.txt", 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

in_file = open("numbers.txt", 'r')
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()