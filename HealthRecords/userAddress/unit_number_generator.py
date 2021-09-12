import random, sys

first_digit_list = [0, 1, 2]

def generate_unit_number():
    hex_sign = "#"
    dash_sign = "-"
    unit_number = []

    unit_number.append(hex_sign)
    unit_number.append(random.randint(0, 2))
    unit_number.append(random.randint(1, 9))
    unit_number.append(dash_sign)

    i = 0
    while i < 3:
        unit_number.append(random.randint(1, 9))
        i += 1

    # print(unit_number)
    return unit_number

def main():
    my_set = set()
    count = 0

    while count < 5000:
        my_set.add(''.join(map(str, generate_unit_number())))
        count = len(my_set)

    sys.stdout = open("unitNumber.csv", "w")
    for n in my_set:
        print(n)
    sys.stdout.close()

main()


