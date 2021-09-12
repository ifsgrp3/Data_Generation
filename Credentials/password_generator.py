# password is required to have a combination of uppercase and
# lowercase letters and numbers
# as well as being between 8 to 20 characters.

import random
import string
import sys


def generate_password():
    # small and big case alphabets with digits
    characters = string.ascii_letters + string.digits

    # length of password can be between 8 to 20
    length = random.randint(8, 20)
    password = ''.join(random.choice(characters) for i in range(length))

    return password


def main():
    count = 0
    my_set = set()
    while count != 5000:
        # To prevent any duplicates in the password generated
        my_set.add(generate_password())
        count = len(my_set)

    sys.stdout = open("password.csv", "w")
    for n in my_set:
        print(n)
    sys.stdout.close()


main()

