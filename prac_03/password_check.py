"""
CP1404/CP5632 - Practical
Program gets a password from user and displays the number of characters as asterisks.
"""

MINIMUM_LENGTH = 3


def main():
    """Passes the password through the necessary functions"""
    password = get_password(MINIMUM_LENGTH)
    convert_to_asterisks(password)


def get_password(MINIMUM_LENGTH):
    password = input("Enter a password with at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        print("That password is too short, it  must be at least {} characters.".format(MINIMUM_LENGTH))
        password = input("Enter a  password: ")
    return password


def convert_to_asterisks(password):
    print('*' * len(password))


main()
