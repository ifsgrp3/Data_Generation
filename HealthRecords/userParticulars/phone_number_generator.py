import random
import sys

first_digit_list = [8, 9]

def generate_contact_number():
    contact_number = []
    first_digit = first_digit_list[random.randint(0, 1)]
    contact_number.append(first_digit)

    i = -0
    while i < 7:
        contact_number.append(random.randint(0, 9))
        i += 1

    return contact_number


def main():
    count = 0
    my_set = set()
    while count != 5000:
        my_set.add(''.join(map(str, generate_contact_number())))
        count = len(my_set)

    sys.stdout = open("PhoneNumber.csv", "w")
    for n in my_set:
        print(n)
    sys.stdout.close()

main()

